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

logger = logging.getLogger('celery_progress')
REDCAP_API_KEYS = ast.literal_eval(settings.REDCAP_API_KEYS)


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
def export_project_data_and_send_email(project_name, emails=[], model_names=[]):

    def get_project_records(project, record_ids):
        try:
            return project.export_records(records=record_ids)
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            time.sleep(5)  # Sleep for a bit before retrying
            return []

    try:
        # Connect to REDCap
        project = Project(
            settings.REDCAP_API_URL, REDCAP_API_KEYS.get(project_name))

        # Export total records to get count
        total_records = project.export_records(fields=['record_id'])
        total_count = len(total_records)
        chunk_size = 500

        all_data = []

        # Setup retry strategy
        retry_strategy = Retry(
            total=10,  # Number of retries
            backoff_factor=10,  # Wait between retries
            status_forcelist=[429, 500, 502, 503, 504],  # Retry on these status codes
            method_whitelist=["HEAD", "GET", "OPTIONS", "POST"]  # Allow retry on these methods
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)

        # Export data in chunks
        for start in range(0, total_count, chunk_size):
            end = start + chunk_size
            record_ids = [record.get('record_id') for record in total_records[start:end]]
            chunk_data = get_project_records(project, record_ids)
            all_data.extend(chunk_data)

        # Process and save data as needed
        tsepamo_data = LoadCSVData()
        tsepamo_data.load_model_data(all_data, model_names)

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
