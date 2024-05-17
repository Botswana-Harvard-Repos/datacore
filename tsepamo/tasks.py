from celery import shared_task
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
    except Exception as exc:
        raise exc
    
