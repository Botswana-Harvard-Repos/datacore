from django.test import TestCase
from tsepamo.models import TsepamoOne,OutcomesOne
from tsepamo.utils import LoadCSVData
from django.test import tag
# Create your tests here.
tag('load')
class TestLoadData(TestCase):


    def setUp(self):
        self.loading = LoadCSVData()
        self.csv_files_models = [('/Users/kebadiretsemotlhabi/source/datacore-project/datacore/Tsepamo 1 copy.csv',['tsepamo.tsepamoone','tsepamo.outcomesone'])]

    def test_load_data_from_csv(self):
        self.loading.load_model_data_all(self.csv_files_models)
        self.assertEqual(TsepamoOne.objects.count(),10)
        
