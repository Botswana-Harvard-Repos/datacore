import logging
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMessage
from celery import shared_task
from tsepamo.utils import LoadCSVData

from .export_utils import GenerateDataExports

logger = logging.getLogger('celery_progress')


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
