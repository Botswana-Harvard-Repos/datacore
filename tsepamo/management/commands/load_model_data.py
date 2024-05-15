from django.core.management.base import BaseCommand
from tsepamo.utils import LoadCSVData


class Command(BaseCommand):
    help = 'Load model data'

    def handle(self, *args, **kwargs):

        csv_files=[('/home/datacore/source/datacore/Tsepamo_1.csv',['tsepamo.tsepamoone','tsepamo.outcomesone'])
                   ('/home/datacore/source/datacore/Tsepamo_2.csv',['tsepamo.tsepamotwo','tsepamo.outcomestwo','tsepamo.switcheripmstwo','tsepamo.personalidentifierstwo','tsepamo.ipms'])
                   ('/home/datacore/source/datacore/Tsepamo_3.csv',['tsepamo.tsepamothree','tsepamo.outcomesthree','tsepamo.switcheripmsthree','personalidentifiersthree'])
                   ('/home/datacore/source/datacore/Tsepamo_4.csv',['tsepamo.tsepamofour','tsepamo.outcomesfour','tsepamo.switcheripmsfour','tsepamo.personalidentifiersfour'])] 
        tsepamo_data = LoadCSVData()
        tsepamo_data.load_model_data_all(csv_files)

        self.stdout.write(self.style.SUCCESS(
            f'Tsepamo data successfully loaded.'))