from django.db import models


class Projects(models.Model):

    name = models.CharField(
        verbose_name='Project Name',
        max_length=20,
        unique=True,
        default='tsepamo_1')

    verbose_name = models.CharField(
        verbose_name='Verbose Project Name',
        max_length=50,
        null=True)

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class InstrumentsMeta(models.Model):

    form_name = models.CharField(
        verbose_name='Instrument Name',
        max_length=100)

    related_project = models.CharField(
        verbose_name='Project Name',
        max_length=20)

    class Meta:
        unique_together = ('form_name', 'related_project', )
        app_label = 'tsepamo'
        verbose_name = 'Instrument Meta Options'
        verbose_name_plural = 'Instrument Meta Options'
