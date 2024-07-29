import os, pytz
from django.apps import apps as django_apps
from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from datetime import datetime

tz = pytz.timezone('Africa/Gaborone')


class ExportFile(models.Model):

    name = models.CharField(
        verbose_name='Export Name',
        max_length=50)

    file = models.FileField(
        upload_to='documents/')

    date_created = models.DateTimeField(
        verbose_name='Date/Time Created',
        default=datetime.now)

    user_created = models.CharField(
        verbose_name='User created',
        max_length=50,
        null=True)

    datetime_started = models.DateTimeField(
        default=datetime.now)

    datetime_completed = models.DateTimeField(
        default=datetime.now)

    download_time = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2)

    download_complete = models.BooleanField(
        default=False,)

    def save(self, *args, **kwargs):
        if self.datetime_started and self.datetime_completed:
            datetime_completed = self.datetime_completed.astimezone(tz)
            datetime_started = self.datetime_started.astimezone(tz)
            difference = datetime_completed - datetime_started
            self.download_time = round(difference.total_seconds() / 60, 2)
        super().save(*args, **kwargs)

    @property
    def export_url(self):
        """Return the file url.
        """
        try:
            return self.file.url
        except ValueError:
            return None

    @property
    def extension(self):
        _, extension = os.path.splitext(self.name)
        return extension

    @property
    def sizify(self):
        """
            Simple kb/mb/gb size snippet for templates:
            {{ export.file.size|sizify }}
        """

        value = self.file.size if self.file else 0
        if value < 512000:
            value = value / 1024.0
            ext = 'Kb'
        elif value < 4194304000:
            value = value / 1048576.0
            ext = 'Mb'
        else:
            value = value / 1073741824.0
            ext = 'Gb'
        return '%s %s' % (str(round(value, 2)), ext)

    @property
    def related_user(self):
        user_model_cls = django_apps.get_model(settings.AUTH_USER_MODEL)
        if self.user_created:
            try:
                user = user_model_cls.objects.get(
                    username=self.user_created)
            except user_model_cls.DoesNotExist:
                return None
            else:
                return user

    @property
    def user_badge(self):
        user = self.related_user
        first_name = getattr(user, 'first_name', None)
        last_name = getattr(user, 'last_name', None)
        if first_name and last_name:
            initials = user.user_initials
            return mark_safe(
                f"<div class='d-flex align-items-center'>"
                f"<div class='user-badge me-2'>{initials}</div>"
                f"<div>{user.first_name} {user.last_name}</div>"
                "</div>")
        return self.user_created

    @property
    def export_status(self):
        if self.download_complete:
            return mark_safe(
                "<span class='badge rounded-pill badge-success'>Ready</span>")
        else:
            return mark_safe(
                "<span class='badge rounded-pill badge-danger'>Pending</span>")

    @property
    def actions(self):
        if self.download_complete:
            return mark_safe(
                "<a class='d-flex align-items-center justify-content-center download-action'"
                    "style='color: #3b5998;' href='#' role='button'>"
                        "<i class='fa-solid fa-download fa-lg'></i>"
                "</a>")

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Export File'
