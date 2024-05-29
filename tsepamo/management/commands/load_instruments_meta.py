from django.core.management.base import BaseCommand

from ...models import InstrumentsMeta, Projects


class Command(BaseCommand):
    help = 'Creates new instruments meta options i.e. relates instruments to project'

    def handle(self, *args, **kwargs):

        projects_data = {'tsepamo_1': ['tsepamoone',
                                       'outcomesone'],
                         'tsepamo_2': ['tsepamotwo',
                                       'outcomestwo',
                                       'switcheripmstwo',
                                       'personalidentifierstwo'],
                         'tsepamo_3': ['tsepamothree',
                                       'outcomesthree',
                                       'switcheripmsthree',
                                       'personalidentifiersthree'],
                         'tsepamo_4': ['tsepamofour',
                                       'outcomesfour',
                                       'switcheripmsfour',
                                       'personalidentifiersfour']}

        for project_name, instruments_list in projects_data.items():
            try:
                Projects.objects.get(name=project_name)
            except Projects.DoesNotExist:
                Projects.objects.create(
                    name=project_name,
                    verbose_name=' '.join(project_name.split('_')).capitalize())

            for instrument in instruments_list:
                try:
                    InstrumentsMeta.objects.get(related_project=project_name,
                                                form_name=instrument)
                except InstrumentsMeta.DoesNotExist:
                    InstrumentsMeta.objects.create(
                        related_project=project_name,
                        form_name=instrument)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully loaded instruments meta'))
