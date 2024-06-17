import csv
from datetime import datetime
from decimal import Decimal
from django.apps import apps as django_apps
from django.db.models import (DateTimeField, DateField, IntegerField,
                              DecimalField)
import logging
logger = logging.getLogger('celery_progress')


class LoadCSVData:
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
        data = []
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                record = {}
                for key, value in row.items():
                    if self.map_choice_data(key, value, record):
                        continue
                    record.update({f'{key}': value})
                data.append(record)
        return data

    def load_model_data(self, data, model_names):
        for model_name in model_names:
            print(f"Model: {model_name}")
            model_cls = django_apps.get_model(model_name)
            model_fields = {f'{field.name}': field for field in model_cls._meta.fields}

            for record in data:
                formatted_record = {}
                for field_name, field in model_fields.items():
                    value = record.get(field_name)
                    if field_name == 'record_id':
                        continue
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
                        value = Decimal(value) if value else value
                    formatted_record[field_name] = None if value == '' else value

                model_objs = model_cls.objects.filter(
                    record_id=record.get('record_id'), )
                if not model_objs:
                #     model_objs.update(**formatted_record)
                # else:
                    create_record = formatted_record.copy()
                    create_record.update(record_id=record.get('record_id'))
                    print(f"Create Record {record.get('record_id')}")
                    model_cls.objects.create(**create_record)

    def load_model_data_all(self, csv_files):
        for csv_file, model_names in csv_files:
            data = self.read_csv_data(csv_file)
            self.load_model_data(data, model_names)


