import os
import datetime
import pandas as pd
from bson.decimal128 import Decimal128
from celery import shared_task, group, chain
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
@shared_task
def prepare_export_data_task(app_label, model_names, export_fields, export_type,
                             export_name, user_emails, export_id):
    fetch_data_tasks = []
    chunk_size = 1000
    for model_name in model_names:
        model_cls = django_apps.get_model(app_label, model_name)
        total_records = model_cls.objects.count()
        for i in range(0, total_records, chunk_size):
            fetch_data_tasks.append(
                fetch_model_data_task.s(app_label, model_name, export_fields, i, i + chunk_size))
    fetch_data_group = group(fetch_data_tasks)

    return chain(
        fetch_data_group | handle_fetch_data_result.s(
            export_type, export_name, user_emails, export_id)).apply_async()


@shared_task
def handle_fetch_data_result(fetch_data_results, export_type, export_name,
                             user_emails, export_id):
    # Merge data in chunks
    chunk_size = 1000  # Adjust chunk size as needed
    all_record_ids = get_unique_record_ids(fetch_data_results)
    chunks = [list(all_record_ids)[i:i + chunk_size] for i in range(0, len(all_record_ids), chunk_size)]

    merge_data_tasks = group(merge_data_chunk_task.s(chunk, fetch_data_results) for chunk in chunks)

    if export_type.lower() == 'csv':
        return chain(
            merge_data_tasks | write_to_csv_task.s(export_name, user_emails, export_id)).apply_async()
    if export_type.lower() == 'excel':
        return chain(
            merge_data_tasks | write_to_excel_task.s(export_name, user_emails, export_id)).apply_async()


@shared_task
def fetch_model_data_task(app_label, model_name, export_fields, start, end):
    """ Returns data related to a specific model, and fields provided.
        @param app_label: name of app model is registered
        @param model_name: name of model
        @return: data dict
    """
    model_cls = django_apps.get_model(app_label, model_name)
    model_fields = get_model_related_fields(model_cls, export_fields)
    data = model_cls.objects.all()[start:end].values(*model_fields)
    return {obj.pop('record_id'): transform_model_data(obj) for obj in data}


@shared_task
def merge_data_chunk_task(chunk, all_model_data):
    """ Returns merged data chunks from different models into a flat table.
        @param chunk: a subset of the data to merge
        @param all_model_data: complete dataset
        @return: data merged by `record_id`
    """
    merged_data = []
    for record_id in chunk:
        record = {'record_id': record_id}
        for model_data in all_model_data:
            model_dict = model_data.get(record_id, {})
            record.update(model_dict)
        merged_data.append(record)
    return merged_data


@shared_task
def write_to_csv_task(records, export_name, user_emails, export_id):
    """ Write data to csv format and returns response """
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


@shared_task
def write_to_excel_task(records, export_name, user_emails, export_id):
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


def transform_model_data(record):
        for key, value in record.items():
            if isinstance(value, Decimal128):
                record[key] = str(value)
        return record


def get_unique_record_ids(all_model_data):
    """ Get a set of all unique record IDs across all models """
    all_record_ids = set()
    for data in all_model_data:
        all_record_ids.update(data.keys())
    return all_record_ids


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
    date_str = current_datetime.strftime('%Y-%m-%d_%H:%M')
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
