from celery import shared_task
from tsepamo.utils import LoadCSVData
import logging
logger = logging.getLogger('celery_progress')

@shared_task()
def run_load_model_data_task():
    logger.debug("The data files")
    csv_files=[('/home/datacore/source/datacore/Tsepamo_1.csv',['tsepamo.tsepamoone','tsepamo.outcomesone']),
                   ('/home/datacore/source/datacore/Tsepamo_2.csv',['tsepamo.tsepamotwo','tsepamo.outcomestwo','tsepamo.switcheripmstwo','tsepamo.personalidentifierstwo','tsepamo.ipmstwo']),
                   ('/home/datacore/source/datacore/Tsepamo_3.csv',['tsepamo.tsepamothree','tsepamo.outcomesthree','tsepamo.switcheripmsthree','personalidentifiersthree']),
                   ('/home/datacore/source/datacore/Tsepamo_4.csv',['tsepamo.tsepamofour','tsepamo.outcomesfour','tsepamo.switcheripmsfour','tsepamo.personalidentifiersfour'])] 
    try:
        tsepamo_data = LoadCSVData()
        logger.debug("Now loading data")
        tsepamo_data.load_model_data_all(csv_files)
    except Exception as exc:
        raise exc
    
