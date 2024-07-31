from django.core.management.base import BaseCommand
from django.forms.models import model_to_dict
from tsepamo.utils import LoadCSVData

from tsepamo.models import (
    TsepamoOne, TsepamoTwo, TsepamoThree, TsepamoFour,
    OutcomesOne, OutcomesTwo, OutcomesThree, OutcomesFour,
    PersonalIdentifiersTwo, PersonalIdentifiersThree, PersonalIdentifiersFour,
    SwitcherIpmsFour, SwitcherIPMSThree, SwitcherIpmsTwo,
    Tsepamo, Outcomes, PersonalIdentifiers, SwitcherIpms
)


class Command(BaseCommand):
    help = 'Migrate data from old models to new models'

    def handle(self, *args, **kwargs):
        self.tsepamo_data = LoadCSVData()
        self.migrate_tsepamo()
        self.migrate_outcomes()
        self.migrate_personal_identifiers()
        self.migrate_switcher_ipms()
        self.stdout.write(self.style.SUCCESS(
            f'Data migration completed successfully'))

    def migrate_tsepamo(self):
        field_mapping = {
            'placental_organism': 'placenta_organism',
            'placental_pcdecid': 'placenta_pcdecid',
            'placental_avascvilli': 'placenta_avascvilli',
            'placental_distalvh': 'placenta_distalvh',
            'placental_fetalmalp': 'placenta_fetalmalp',
            'was_this_woman_on_aspirin': 'was_this_woman_aspirin',
            # add all relevant field mappings here
        }
        self.migrate_model(
            [TsepamoOne, TsepamoTwo, TsepamoThree, TsepamoFour], Tsepamo, field_mapping)

    def migrate_outcomes(self):
        self.migrate_model(
            [OutcomesOne, OutcomesTwo, OutcomesThree, OutcomesFour], Outcomes)

    def migrate_personal_identifiers(self):
        self.migrate_model([PersonalIdentifiersTwo, PersonalIdentifiersThree,
                           PersonalIdentifiersFour], PersonalIdentifiers)

    def migrate_switcher_ipms(self):
        self.migrate_model(
            [SwitcherIpmsTwo, SwitcherIPMSThree, SwitcherIpmsFour], SwitcherIpms)

    def migrate_model(self, old_models, new_model, field_mapping=None):
        print(new_model, old_models)
        for old_model in old_models:
            for obj in old_model.objects.all():
                data = model_to_dict(obj)
                # Remove the primary key to avoid conflicts
                data.pop('id', None)
                if field_mapping:
                    transformed_data = {field_mapping.get(
                        k, k): v for k, v in data.items()}
                    if transformed_data:
                        self.format_all_fields(new_model, transformed_data)
                        new_model.objects.create(**transformed_data)
                else:
                    self.format_all_fields(new_model, data)
                    new_model.objects.create(**data)

    def format_all_fields(self, model, data):
        model_fields = {field.name: field for field in model._meta.fields}
        formatted_data = {}

        for field_name, field in model_fields.items():
            value = data.get(field_name)
            if field_name == 'record_id':
                continue
            formatted_data[field_name] = self.tsepamo_data.format_fields(
                field, value)

        data.update(formatted_data)
