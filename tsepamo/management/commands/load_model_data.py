from django.core.management.base import BaseCommand
from tsepamo.tasks import run_load_model_data_task


class Command(BaseCommand):
    help = 'Load model data'

    def handle(self, *args, **kwargs):

        run_load_model_data_task.delay()

        self.stdout.write(self.style.SUCCESS(
            f'Tsepamo data successfully loaded.'))
