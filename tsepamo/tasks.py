from celery import shared_task,current_task
from django.core.management import call_command
import logging
logger = logging.getLogger(__name__)
from tsepamo.utils import LoadCSVData

@shared_task(bind=True)
def run_load_model_data_task(self):
    csv_files=[('/home/datacore/source/datacore/Tsepamo_1.csv',['tsepamo.tsepamoone','tsepamo.outcomesone']),
                   ('/home/datacore/source/datacore/Tsepamo_2.csv',['tsepamo.tsepamotwo','tsepamo.outcomestwo','tsepamo.switcheripmstwo','tsepamo.personalidentifierstwo','tsepamo.ipms']),
                   ('/home/datacore/source/datacore/Tsepamo_3.csv',['tsepamo.tsepamothree','tsepamo.outcomesthree','tsepamo.switcheripmsthree','personalidentifiersthree']),
                   ('/home/datacore/source/datacore/Tsepamo_4.csv',['tsepamo.tsepamofour','tsepamo.outcomesfour','tsepamo.switcheripmsfour','tsepamo.personalidentifiersfour'])] 
    try:
        tsepamo_data = LoadCSVData()
        tsepamo_data.load_model_data_all(csv_files)

        current_task.update_state(
            state='PROGRESS',
            meta={'current': 1, 'total': 1} 
        )
        result = "Data loading completed successfully"
        return {'result': result}
    except Exception as exc:
        logger.exception("An error occured during loading data")
        raise exc
    
