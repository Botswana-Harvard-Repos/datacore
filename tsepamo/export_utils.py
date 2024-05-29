import os
import pandas as pd
import datetime
from django.apps import apps as django_apps
from django.conf import settings
from django.http.response import HttpResponse

from .models import ExportFile


upload_folder = settings.MEDIA_ROOT


class GenerateDataExports:
    """ Generate data to different file formats, with either a select subset
        of fields or all the model fields.
    """

    def __init__(self, export_name, user_created, app_label='', export_types=[], model_names=[], export_fields=[]):
        self.export_model_cls = ExportFile
        self.export_types = export_types
        self.export_name = export_name
        self.model_names = model_names
        self.export_fields = export_fields
        self.app_label = app_label
        self.user_created = user_created
        self.export_data = []

        if self.export_fields and self.model_names and self.export_types and self.export_name:
            self.export_data = self.prepare_export_data()

    @property
    def exclude_fields(self):
        return ['id']

    def get_model_related_fields(self, model_cls):
        model_fields = [field.name for field in model_cls._meta.fields]
        related_fields = [field for field in self.export_fields if field in model_fields]
        return related_fields

    def get_model_data(self, model_name):
        model_cls = django_apps.get_model(self.app_label, model_name)
        related_fields = self.get_model_related_fields(model_cls)
        if related_fields:
            fields = ['record_id', ] + related_fields
            return {obj.pop('record_id'): obj for obj in model_cls.objects.values(*fields)}

    def generate_exports(self):
        for export_type in self.export_types:
            if export_type.lower() == 'csv':
                return self.write_to_csv(self.export_data)

    def prepare_export_data(self):
        all_model_data = []
        for model_name in self.model_names:
            _model_data = self.get_model_data(model_name)
            if _model_data:
                all_model_data.append(_model_data)

        all_record_ids = set()
        # Get a set of all unique record IDs across all models
        for data in all_model_data:
            all_record_ids.update(data.keys())

        # Merge data based on record_id
        merged_data = []
        for record_id in all_record_ids:
            record = {'record_id': record_id}
            for model_data in all_model_data:
                model_dict = model_data.get(record_id, {})
                record.update(model_dict)
            merged_data.append(record)

        return merged_data

    def write_to_csv(self, records):
        """ Write data to csv format and returns response
        """
        df = pd.DataFrame(records)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={self.get_export_filename()}.csv'
        df.to_csv(path_or_buf=response, index=False)
        self.handle_export_response(response)
        return response

    def handle_export_response(self, response, export_type='csv'):
        file_path = f'{upload_folder}/documents'
        file_name = f'{self.get_export_filename()}.{export_type}'

        if not response:
            print(f'Empty response returned for {self.export_name} exports.')

        if response.status_code == 200:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with open(f'{file_path}/{file_name}', 'wb') as file:
                file.write(response.content)
            # Create model instance for export file generated.
            self.create_export_model_instance(export_file=file_name)
        else:
            response.raise_for_status()

    def get_export_filename(self):
        date_str = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
        filename = "%s-%s" % (self.export_name, date_str)
        return filename

    def create_export_model_instance(self, export_file):
        upload_to = self.export_model_cls.file.field.upload_to
        self.export_model_cls.objects.create(
            name=export_file,
            download_complete=True,
            user_created=self.user_created,
            file=upload_to + export_file, )
