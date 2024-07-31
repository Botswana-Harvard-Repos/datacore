import os
import datetime
import pandas as pd
from bson.decimal128 import Decimal128
from celery import shared_task, group, chain
from celery.exceptions import SoftTimeLimitExceeded
from collections import defaultdict
from django.core.mail import EmailMessage
from django.apps import apps as django_apps
from django.conf import settings
from django.http.response import HttpResponse, JsonResponse
from io import BytesIO

from .models import ExportFile

upload_folder = settings.MEDIA_ROOT


class GenerateDataExports:
    """ Generate data to different file formats, with either a select subset
        of fields or all the model fields.
    """

    def __init__(self, export_name, user_created, app_label='', user_emails=[],
                 export_type='csv', model_names=[], export_fields=[]):
        self.export_model_cls = ExportFile
        self.export_type = export_type
        self.export_name = export_name
        self.model_names = model_names or []
        self.export_fields = export_fields
        self.app_label = app_label
        self.user_created = user_created
        self.user_emails = user_emails
        self.export_data = []

        exclude_models = ['exportfile', 'projects', 'instrumentsmeta']
        if not self.model_names:
            app_models = django_apps.get_app_config(app_label).models
            for name, _ in app_models.items():
                if name in exclude_models:
                    continue

                self.model_names.append(name)

        if self.model_names and self.export_type and self.export_name:
            self.generate_exports()

    @property
    def exclude_fields(self):
        return ['id']

    def generate_exports(self):
        export_file = self.create_export_model_instance()

        prepare_export_data_task.delay(
            self.app_label, self.model_names, self.export_fields,
            self.export_type, self.export_name, self.user_emails, export_file.id)

        return JsonResponse({'status': 'Export data preparation task started'})

    def create_export_model_instance(self):
        file_name = f'{get_export_filename(self.export_name)}.{self.export_type}'
        upload_to = self.export_model_cls.file.field.upload_to
        return self.export_model_cls.objects.create(
            name=file_name,
            user_created=self.user_created,
            file=upload_to + file_name, )


# Main task to orchestrate the data preparation and export
@shared_task(bind=True, soft_time_limit=7000, time_limit=7200)
def prepare_export_data_task(self, app_label, model_names, export_fields,
                             export_type, export_name, user_emails, export_id):
    data = defaultdict(dict)
    try:
        chunk_size = 10000
        for model_name in model_names:
            model_cls = django_apps.get_model(app_label, model_name)
            offset = 0
            while True:
                records = fetch_model_data(model_cls, export_fields, offset, chunk_size)
                if not records:
                    break
                for record in records:
                    record_id = record.pop('record_id')
                    print(record_id)
                    data[record_id].update(record)
                offset += chunk_size

        merged_data = []
        for record_id, record_data in data.items():
            print(record_id)
            merged_data.append(
                {'record_id': record_id, **record_data})

        if export_type.lower() == 'csv':
            write_to_csv(merged_data, export_name, user_emails, export_id)
        if export_type.lower() == 'excel':
            write_to_excel_task(merged_data, export_name, user_emails, export_id)
    except SoftTimeLimitExceeded:
        self.update_state(state='FAILURE')
        new_soft_time_limit = self.request.soft_time_limit + 3600
        new_time_limit = self.request.time_limit + 3600
        self.retry(countdown=10, max_retries=3, soft_time_limit=new_soft_time_limit, time_limit=new_time_limit)


def get_unique_record_ids(app_label, model_names):
    unique_record_ids = set()
    for model_name in model_names:
        model_cls = django_apps.get_model(app_label, model_name)
        unique_record_ids.update(
            model_cls.objects.values_list('record_id', flat=True))
    return unique_record_ids


def write_to_csv(records: list, export_name, user_emails, export_id):
    """ Write data to csv format and returns response
    """
    df = pd.DataFrame(records)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={get_export_filename(export_name)}.csv'
    df.to_csv(path_or_buf=response, index=False)
    try:
        handle_export_response(response, export_name)
    except Exception as e:
        print('failed writing to file, with error:', e)
    else:
        send_email_task.delay(export_name, user_emails, export_id)
    return response


def write_to_excel_task(records: list, export_name, user_emails, export_id):
    """ Write data to excel format and returns response
    """
    excel_buffer = BytesIO()
    writer = pd.ExcelWriter(excel_buffer, engine='openpyxl')

    df = pd.DataFrame(records)
    df.to_excel(writer, sheet_name=f'{export_name}', index=False)

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

    response['Content-Disposition'] = f'attachment; filename={get_export_filename(export_name)}.xlsx'
    try:
        handle_export_response(response, export_name, export_type='xlsx')
    except Exception as e:
        print('failed writing to file, with error:', e)
    else:
        send_email_task.delay(export_name, user_emails, export_id)
    return response


def fetch_model_data(model_cls, export_fields, offset=0, limit=10000):
    model_fields = get_model_related_fields(model_cls, export_fields)
    return list(model_cls.objects.values(*model_fields)[offset:offset + limit])


@shared_task
def send_email_task(export_name, user_emails, export_id):
    email = EmailMessage('DataCore export ready',
                         f'{export_name} has been successfully generated and ready for download',
                         settings.DEFAULT_FROM_EMAIL,
                         user_emails)

    try:
        email.send()
    except Exception as e:
        print(f'Error sending email: {str(e)}')

    try:
        export_file = ExportFile.objects.get(id=export_id)
    except ExportFile.DoesNotExist:
        raise
    else:
        export_file.datetime_completed = datetime.datetime.now()
        export_file.download_complete = True
        export_file.save()


def get_model_related_fields(model_cls, export_fields):
    """ Returns fields related to a model class, if specific fields
        are required returns only a subset of those fields.
        @param model_cls: model class
        @param export_fields: subset fields of interest.
        @return: fields related to the model class
    """
    model_fields = [field.name for field in model_cls._meta.fields]
    if not export_fields:
        return model_fields
    related_fields = [field for field in export_fields if field in model_fields]
    return related_fields


def handle_export_response(response, export_name, export_type='csv'):
        file_path = f'{upload_folder}/documents'
        file_name = f'{get_export_filename(export_name)}.{export_type}'

        if not response:
            print(f'Empty response returned for {export_name} exports.')

        if response.status_code == 200:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with open(f'{file_path}/{file_name}', 'wb') as file:
                file.write(response.content)
        else:
            response.raise_for_status()


def get_export_filename(export_name):
    current_datetime = datetime.datetime.now()
    date_str = current_datetime.strftime('%Y-%m-%d_%H_%M')
    filename = "%s-%s" % (export_name, date_str)
    return filename


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
