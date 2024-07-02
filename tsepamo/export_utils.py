import os
import pandas as pd
import datetime
from django.apps import apps as django_apps
from django.conf import settings
from django.http.response import HttpResponse
from io import BytesIO

from .models import ExportFile

upload_folder = settings.MEDIA_ROOT


class GenerateDataExports:
    """ Generate data to different file formats, with either a select subset
        of fields or all the model fields.
    """

    def __init__(self, export_name, user_created, app_label='', export_type='csv', model_names=[], export_fields=[]):
        self.export_model_cls = ExportFile
        self.export_type = export_type
        self.export_name = export_name
        self.model_names = model_names
        self.export_fields = export_fields
        self.app_label = app_label
        self.user_created = user_created
        self.export_data = []

        if self.export_fields and self.model_names and self.export_type and self.export_name:
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
        if self.export_type.lower() == 'csv':
            return self.write_to_csv(self.export_data)
        if self.export_type.lower() == 'excel':
            return self.write_to_excel(self.export_data)

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

    def write_to_excel(self, records):
        """ Write data to excel format and returns response
        """
        excel_buffer = BytesIO()
        writer = pd.ExcelWriter(excel_buffer, engine='openpyxl')

        df = pd.DataFrame(records)
        df.to_excel(writer, sheet_name=f'{self.export_name}', index=False)

        # Save and close the workbook
        writer.close()

        # Seek to the beginning and read to copy the workbook to a variable in memory
        excel_buffer.seek(0)
        workbook = excel_buffer.read()

        # Create an HTTP response with the Excel file as an attachment
        response = HttpResponse(
            workbook,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        response['Content-Disposition'] = f'attachment; filename={self.get_export_filename()}.xlsx'
        self.handle_export_response(response, export_type='xlsx')
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
            # self.create_export_model_instance(export_file=file_name)
        else:
            response.raise_for_status()

    def get_export_filename(self):
        current_datetime = datetime.datetime.now()
        date_str = current_datetime.strftime('%Y-%m-%d_%H:%M')
        filename = "%s-%s" % (self.export_name, date_str)
        return filename

    def create_export_model_instance(self, export_type):
        file_name = f'{self.get_export_filename()}.{export_type}'
        upload_to = self.export_model_cls.file.field.upload_to
        return self.export_model_cls.objects.create(
            name=file_name,
            user_created=self.user_created,
            file=upload_to + file_name, )


def generate_model_data_dict(model_name):

    def write_to_csv(records, filename):
        """ Write data to csv format and returns response
        """
        df = pd.DataFrame(records)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={filename}.csv'
        df.to_csv(path_or_buf=response, index=False)
        return response

    model_cls = django_apps.get_model('tsepamo', model_name)
    # Define the output file
    output_file = f'{model_name.lower()}_data_dictionary.csv'

    records = []

    for field in model_cls._meta.fields:
        field_name = field.name
        field_type = field.get_internal_type()
        max_length = getattr(field, 'max_length', '')
        other_attributes = []

        # Check for other relevant field attributes
        if field.blank:
            other_attributes.append('blank=True')
        if field.null:
            other_attributes.append('null=True')
        if hasattr(field, 'auto_now_add') and field.auto_now_add:
            other_attributes.append('auto_now_add=True')
        if hasattr(field, 'auto_now') and field.auto_now:
            other_attributes.append('auto_now=True')

        # Write the row for this field
        records.append({
            'Form Name': model_name,
            'Field Name': field_name,
            'Field Type': field_type,
            'Max Length': max_length,
            'Other Attributes': ', '.join(other_attributes)
        })

    return write_to_csv(records, output_file)
