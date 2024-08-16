from django.core.management.base import BaseCommand, CommandError

from tsepamo.tasks import export_project_data_and_send_email

project_models_map = {'tsepamo_1': ['tsepamo.tsepamo', 'tsepamo.outcomes'],
                      'tsepamo_2': ['tsepamo.tsepamo', 'tsepamo.outcomes',
                                    'tsepamo.switcheripms', 'tsepamo.personalidentifiers', 'tsepamo.ipmstwo'],
                      'tsepamo_3': ['tsepamo.tsepamo', 'tsepamo.outcomes',
                                    'tsepamo.switcheripms', 'tsepamo.personalidentifiers'],
                      'tsepamo_4': ['tsepamo.tsepamo', 'tsepamo.outcomes',
                                    'tsepamo.switcheripms', 'tsepamo.personalidentifiers']}


class Command(BaseCommand):
    help = 'Pull data and populate model instances from redcap'

    def add_arguments(self, parser):
        parser.add_argument('--project_names',
                            nargs="+",
                            type=str,
                            help='Specify project name')

        # emails to send outcomes to
        parser.add_argument('--emails',
                            type=str,
                            nargs="+",
                            required=True,
                            help='Email address of registered users')

    def handle(self, *args, **options):
        project_names = options.get('project_names', None)
        if not project_names:
            project_names = project_models_map.keys()
        emails = options['emails']

        for project_name, models in project_models_map.items():
            if project_name not in project_names:
                continue

            try:
                export_project_data_and_send_email.delay(project_name, emails, models)
            except Exception as e:
                raise CommandError(
                    f'Failed to pull data for {project_name} with {e}, check logs.')
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'Tsepamo data pulled successfully, for {project_name}'))
