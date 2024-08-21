import ast
import logging
import requests
import time
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMessage
from celery import shared_task
from redcap import Project
from requests.adapters import HTTPAdapter, Retry
from tsepamo.utils import LoadCSVData
from .export_utils import GenerateDataExports
from pymongo import MongoClient
import os

logger = logging.getLogger('celery_progress')
REDCAP_API_KEYS = ast.literal_eval(settings.REDCAP_API_KEYS)

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]


@shared_task()
def run_load_model_data_task():
    logger.debug("The data files")

    csv_files = [('/home/datacore/source/datacore/Tsepamo_1.csv',
                  ['tsepamo.tsepamoone', 'tsepamo.outcomesone']),
                 ('/home/datacore/source/datacore/Tsepamo_2.csv',
                  ['tsepamo.tsepamotwo', 'tsepamo.outcomestwo', 'tsepamo.switcheripmstwo',
                   'tsepamo.personalidentifierstwo', 'tsepamo.ipmstwo']),
                 ('/home/datacore/source/datacore/Tsepamo_3.csv',
                  ['tsepamo.tsepamothree', 'tsepamo.outcomesthree', 'tsepamo.switcheripmsthree',
                   'tsepamo.personalidentifiersthree']),
                 ('/home/datacore/source/datacore/Tsepamo_4.csv',
                  ['tsepamo.tsepamofour', 'tsepamo.outcomesfour', 'tsepamo.switcheripmsfour',
                   'tsepamo.personalidentifiersfour'])]

    try:
        tsepamo_data = LoadCSVData()
        logger.debug("Now loading data")
        tsepamo_data.load_model_data_all(csv_files)
    except Exception as exc:
        raise exc


@shared_task
def generate_exports(export_name, user_created, user_emails=[], app_label='', export_type='csv',
                     model_names=[], export_fields=[]):

    export_cls = GenerateDataExports(
        export_name, user_created, app_label, export_type,
        model_names, export_fields, )
    export_file = export_cls.create_export_model_instance(export_type)

    export_cls.generate_exports()

    email = EmailMessage('DataCore export ready',
                         f'{export_name} has been successfully generated and ready for download',
                         settings.DEFAULT_FROM_EMAIL,
                         user_emails)
    email.send()
    export_file.datetime_completed = datetime.now()
    export_file.download_complete = True
    export_file.save()


@shared_task
def export_project_data_and_send_email(project_name, emails=[], collection_name=None):

    def get_metadata(project):
        try:
            return project.export_metadata()
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            time.sleep(5)  # Sleep for a bit before retrying
            return []

    def get_project_records(project, record_ids):
        try:
            return project.export_records(records=record_ids)
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            time.sleep(5)  # Sleep for a bit before retrying
            return []

    def download_file(project, record_id, field_name):
        try:
            content, _ = project.export_file(record_id, field_name)
            return content
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            time.sleep(5)  # Sleep for a bit before retrying
            return []

    def update_or_create_model(project, collection_name, record, file_fields):
        record_id = record['record_id']
        collection = db[collection_name]

        for field in file_fields:
            if field in record and record[field]:
                file_content = download_file(project, record_id, field)
                file_name = f"{record_id}_{field}.jpg"
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)

                with open(file_path, 'wb') as f:
                    f.write(file_content)
                record[field] = file_path

        print(f"Create Record {record_id}")
        collection.update_one(
            {'record_id': record_id},  # Search for a record with this ID
            {'$set': record},  # Update the record with new data
            upsert=True  # Create the record if it doesn't exist
            )
    try:
        # Connect to REDCap
        project = Project(
            settings.REDCAP_API_URL, REDCAP_API_KEYS.get(project_name))

        # Export total records to get count
        total_records = project.export_records(fields=['record_id'])
        total_count = len(total_records)
        chunk_size = 500

        # Get metadata and determine file fields
        metadata = get_metadata(project)
        file_fields = [field['field_name']
                       for field in metadata if field['field_type'] == 'file']

        # Setup retry strategy
        retry_strategy = Retry(
            total=10,  # Number of retries
            backoff_factor=10,  # Wait between retries
            # Retry on these status codes
            status_forcelist=[429, 500, 502, 503, 504],
            # Allow retry on these methods
            method_whitelist=["HEAD", "GET", "OPTIONS", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)

        # Export data in chunks
        for start in range(0, total_count, chunk_size):
            end = start + chunk_size
            record_ids = [record.get('record_id')
                          for record in total_records[start:end]]
            chunk_data = get_project_records(project, record_ids)
            for record in chunk_data:
                update_or_create_model(collection_name, record, file_fields)

        # Send success email notification
        success_email = EmailMessage(
            'Project Data Export Complete',
            f'The export of project data {project_name} is complete.',
            settings.DEFAULT_FROM_EMAIL,
            emails,
        )
        success_email.send()
    except Exception as e:
        # Log the error and send a failure notification email
        print(f"An error occurred: {e}")
        failure_email = EmailMessage(
            'Tsepamo data export has failed',
            f'The export of project data {project_name} has failed. Please check log info.',
            settings.DEFAULT_FROM_EMAIL,
            emails,
        )
        failure_email.send()
        raise e
