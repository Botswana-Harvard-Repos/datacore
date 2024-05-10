from django.core.management.base import BaseCommand
from utils import LoadCSVData


class Command(BaseCommand):
    help = 'Load model data'

    def handle(self, *args, **kwargs):

        csv_files=[('/Users/kebadiretsemotlhabi/source/datacore-project/datacore/Tsepamo 1.csv',['tsepamo.tsepamoone','tsepamo.outcomesone'])
                   ('/Users/kebadiretsemotlhabi/source/datacore-project/datacore/Tsepamo 2.csv',['tsepamo.tsepamotwo','tsepamo.outcomestwo','tsepamo.switcheripmstwo','tsepamo.personalidentifierstwo','tsepamo.ipms'])
                   ('/Users/kebadiretsemotlhabi/source/datacore-project/datacore/Tsepamo 3.csv',['tsepamo.tsepamothree','tsepamo.outcomesthree','tsepamo.switcheripmsthree','personalidentifiersthree'])
                   ('/Users/kebadiretsemotlhabi/source/datacore-project/datacore/Tsepamo 4.csv',['tsepamo.tsepamofour','tsepamo.outcomesfour','tsepamo.switcheripmsfour','tsepamo.personalidentifiersfour'])] 
        tsepamo_data = LoadCSVData()
        tsepamo_data.load_model_data_all(csv_files)

        self.stdout.write(self.style.SUCCESS(
            f'Tsepamo data successfully loaded.'))