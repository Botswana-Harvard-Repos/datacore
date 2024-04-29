from django.db import models

from tsepamo.models.record_id_model_mixin import RecordIDModelMixin


class SwitcherIpmsTwo(RecordIDModelMixin, models.Model):
    ipms_foundv1 = models.CharField(
        verbose_name="Patient's record found in IPMS?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    cd4any = models.CharField(
        verbose_name="Are any CD4s found in IPMS (before delivery)?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    recentcd4 = models.PositiveIntegerField(
        verbose_name="What is the most recent CD4 cell count measurement on or prior to "
                     "\"date_switch\"?",
        blank=True, null=True,
        help_text="", )

    recentcd4date = models.DateField(
        verbose_name="What is the date of the most recent CD4 cell count measurement on "
                     "or prior to \"date_switch\"?",
        blank=True, null=True,
        help_text="MM-DD-YY", )

    cd42016 = models.PositiveIntegerField(
        verbose_name="What is the most recent CD4 cell count measurement on or prior to "
                     "1 January 2016?",
        blank=True, null=True,
        help_text="", )

    cd42016date = models.DateField(
        verbose_name="What is the date of the most recent CD4 cell count measurement on "
                     "or prior to 1 January 2016?",
        blank=True, null=True,
        help_text="MM-DD-YY", )

    cd4nadir = models.PositiveIntegerField(
        verbose_name="What is the lowest recorded CD4 cell count measurement?",
        help_text="", )

    cd4nadirdate = models.DateField(
        verbose_name="What is the date of the lowest recorded CD4 value?",
        help_text="MM-DD-YY", )

    vlany = models.CharField(
        verbose_name="Are any Viral Loads found in IPMS (before delivery)?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    recentrnayesno = models.CharField(
        verbose_name="Is there a Viral Load measurement on or prior to \"date_switch\"?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    recentrnadate = models.DateField(
        verbose_name="What is the date of the most recent Viral Load measurement on or "
                     "prior to \"date_switch\"?",
        blank=True, null=True,
        help_text="MM-DD-YY", )

    recentrna_undetectable = models.CharField(
        verbose_name="Is the most recent Viral Load measurement on or prior to "
                     "\"date_switch\" undetectable (<400 or <50 or <25)?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    recentrna_undetect_value = models.CharField(
        verbose_name="What is the threshold for the undetectable Viral Load?",
        max_length=1,
        choices=(('1', '< 400 or less than 400'), ('2', '< 50 or less than 50'),
                 ('3', '< 25 or less than 25'), ('0', '0'), ('4', 'Other')),
        blank=True, null=True,
        help_text="", )

    recentrna = models.PositiveIntegerField(
        verbose_name="What is the most recent Viral Load measurement on or prior to "
                     "\"date_switch\"?",
        blank=True, null=True,
        help_text="", )

    rna2016yesno = models.CharField(
        verbose_name="Is there a Viral Load measurement on or prior to 1 January 2016?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    rna2016date = models.DateField(
        verbose_name="What is the date of the most recent Viral Load measurement on or "
                     "prior to 1 January 2016?",
        blank=True, null=True,
        help_text="MM-DD-YY", )

    rna2016_undetectable = models.CharField(
        verbose_name="Is the most recent Viral Load measurement on or prior to 1 "
                     "January 2016 undetectable (< 400 or < 50 or < 25)?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    rna2016_undetect_value = models.CharField(
        verbose_name="What is the threshold for the undetectable Viral Load?",
        max_length=1,
        choices=(('1', '< 400 or less than 400'), ('2', '< 50 or less than 50'),
                 ('3', '< 25 or less than 25'), ('0', '0'), ('4', 'Other')),
        blank=True, null=True,
        help_text="", )

    rna2016 = models.PositiveIntegerField(
        verbose_name="What is the most recent Viral Load measurement on or prior to 1 "
                     "January 2016?",
        blank=True, null=True,
        help_text="", )

    ipms_addinfov1 = models.TextField(
        verbose_name="Any additional information from IPMS?",
        blank=True, null=True,
        help_text="", )

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Switcher IPMS 2'
        verbose_name_plural = 'Switcher IPMS 2'