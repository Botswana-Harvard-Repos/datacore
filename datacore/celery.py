import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datacore.settings")
app = Celery("datacore")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

