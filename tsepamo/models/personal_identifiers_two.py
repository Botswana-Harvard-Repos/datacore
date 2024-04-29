from django.db import models

from tsepamo.models.record_id_model_mixin import RecordIDModelMixin


class PersonalIdentifiersTwo(RecordIDModelMixin, models.Model):
    hivneg_pi = models.CharField(
        verbose_name="Is this woman HIV-positive?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="If HIV status unknown, choose 'NO'", )

    pi_citizen = models.CharField(
        verbose_name="Is this woman a Botswana citizen?  Or is she married to a "
                     "Botswana citizen and therefore received HIV and ANC care within "
                     "the Botswana government system?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="Answer yes if the participant in a non-citizen but got her care "
                  "through the government and is likely to be able to be found in IMPS", )

    omang = models.PositiveIntegerField(
        verbose_name="OMANG",
        help_text="if patient has no OMANG, leave BLANK", )

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=100,
        help_text="If unknown, write UNKNOWN", )

    middle_name = models.CharField(
        verbose_name="Middle Name",
        max_length=100,
        blank=True, null=True,
        help_text="", )

    surname = models.CharField(
        verbose_name="Surname",
        max_length=100,
        help_text="If unknown, write UNKNOWN", )

    birthdate = models.DateField(
        verbose_name="Birthdate",
        help_text="MM DD YEAR", )

    pi_idccclinic = models.TextField(
        verbose_name="Name of IDCC clinic?",
        help_text="if unknown, write unknown", )

    la_pi = models.CharField(
        verbose_name="Medical Record Number 1? (_A number, the first letter will depend "
                     "on site.  For example at SLH this is LA number)",
        max_length=100,
        blank=True, null=True,
        help_text="If unknown leave blank", )

    pm_pi = models.CharField(
        verbose_name="Medical Record Number 2? (_M number, the first letter will depend "
                     "on site.  For example at SLH this is LM number)",
        max_length=100,
        blank=True, null=True,
        help_text="If unknown leave blank", )

    other_info_pi = models.TextField(
        verbose_name="Other information",
        blank=True, null=True,
        help_text="any clarifications or information that may be helpful ", )

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Personal Identifiers 2'
        verbose_name_plural = 'Personal Identifiers 2'
