import csv
from datetime import datetime, date
from django.apps import apps as django_apps
from django.db.models import (DateTimeField, DateField, IntegerField,
                              DecimalField)


class LoadCSVData:

    def __init__(self):
        self.data = []

    def map_choice_data(self, key, value, record):
        is_choice = key.split('___')
        if len(is_choice) > 1:
            key = is_choice[0]
            value = is_choice[1].strip() if value == '1' else None
            dict_value = record.setdefault(key, value)

            if value and dict_value and dict_value != value:
                list_value = dict_value.split(', ')
                list_value.append(value)
                record[key] = ', '.join(list_value)
            return True
        return False

    def read_csv_data(self, csv_file):
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                record = {}
                for key, value in row.items():
                    if self.map_choice_data(key, value, record):
                        continue
                    record.update({f'{key}': value})
                self.data.append(record)
        return self.data

    def load_model_data(self, data, model_name):
        model_cls = django_apps.get_model(model_name)
        model_fields = {f'{field.name}': field for field in model_cls._meta.fields}
        for record in data:
            formatted_record = {}
            for field_name, field in model_fields.items():
                value = record.get(field_name)
                if isinstance(field, DateTimeField):
                    try:
                        value = datetime.strptime(value, '%Y-%m-%d %H:%M') if value else value
                    except TypeError:
                        pass
                if isinstance(field, DateField):
                    try:
                        value = datetime.strptime(value, '%Y-%m-%d').date() if value else value
                    except TypeError:
                        pass
                if isinstance(field, IntegerField):
                    value = int(value) if value else value
                if isinstance(field, DecimalField):
                    value = float(value) if value else value
                formatted_record[field_name] = None if value == '' else value

            model_cls.objects.update_or_create(
                record_id=record.get('record_id'), defaults=formatted_record)
