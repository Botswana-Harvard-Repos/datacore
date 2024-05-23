import os
import pandas as pd
import datetime
from django.apps import apps as django_apps
from django.http.response import HttpResponse


class GenerateDataExports:
    """ Generate data to different file formats, with either a select subset
        of fields or all the model fields.
    """

    def __init__(self, app_label='', model_name='', export_fields=[]):
        self.model_cls = django_apps.get_model(app_label, model_name)
        self.export_fields = export_fields
        self.app_label = app_label
        self.model_name = model_name

    def export_as_csv(self):
        records = []
        if self.export_fields:
            records = self.model_cls.objects.values(*self.export_fields)
        else:
            records = self.model_cls.objects.all()

        return self.write_to_csv(records)

    def write_to_csv(self, records):
        """ Write data to csv format and returns response
        """
        df = pd.DataFrame(records)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={self.get_export_filename()}.csv'
        df.to_csv(path_or_buf=response, index=False)
        self.handle_export_response(response)
        return response

    def handle_export_response(self, response):
        file_path = f'{self.app_label}/media/admin_exports/{self.app_label}_{self.model_name}'

        if not response:
            print(f'Empty response returned for {self.model_cls._meta.verbose_name}')

        if response.status_code == 200:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with open(f'{file_path}/{self.get_export_filename()}.csv', 'wb') as file:
                file.write(response.content)
        else:
            response.raise_for_status()

    def get_export_filename(self):
        date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        filename = "%s-%s" % (self.model_cls.__name__, date_str)
        return filename
