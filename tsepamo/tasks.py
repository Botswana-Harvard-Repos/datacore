from celery import shared_task
from django.core.management import call_command
import logging
logger = logging.getLogger(__name__)

@shared_task(bind=True)
def run_load_model_data_task(self):
    try:
        call_command('load_model_data')
    except Exception as exc:
        logger.exception("An error occured during loading data")
        raise exc
    
