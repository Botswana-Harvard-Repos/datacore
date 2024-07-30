from django.db import models

from .model_mixins import CompleteFieldMixin, UuidModelMixin, RecordIDModelMixin


class IpmsTwo(UuidModelMixin, RecordIDModelMixin, CompleteFieldMixin, models.Model):

    ipms_found = models.CharField(
        verbose_name="Patient's record found in IPMS?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    ipms_height = models.CharField(
        verbose_name="Patient's Height? (in meters with 2 decimal points)",
        max_length=100,
        blank=True, null=True,
        help_text="", )

    ipms_wt = models.PositiveIntegerField(
        verbose_name="Pre-Pregnancy Weight? (in KG, no decimal points)",
        blank=True, null=True,
        help_text="", )

    ipms_wtdate = models.DateField(
        verbose_name="Pre-Pregnancy Weight Date?",
        help_text="MM-DD-YY", )

    ipms_cd4num = models.PositiveIntegerField(
        verbose_name="How many CD4s are found in IPMS (before delivery)?",
        help_text="", )

    ipms_cd41 = models.PositiveIntegerField(
        verbose_name="CD4 1 (most recent)",
        help_text="", )

    ipms_cd4date1 = models.DateField(
        verbose_name="CD4 1 date?",
        help_text="MM-DD-YY", )

    ipms_cd42 = models.PositiveIntegerField(
        verbose_name="CD4 2",
        help_text="", )

    ipms_cd4date2 = models.DateField(
        verbose_name="CD4 2 date?",
        help_text="MM-DD-YY", )

    ipms_cd43 = models.PositiveIntegerField(
        verbose_name="CD4 3",
        help_text="", )

    ipms_cd4date3 = models.DateField(
        verbose_name="CD4 3 date?",
        help_text="MM-DD-YY", )

    ipms_cd44 = models.PositiveIntegerField(
        verbose_name="CD4 4",
        help_text="", )

    ipms_cd4date4 = models.DateField(
        verbose_name="CD4 4 date?",
        help_text="MM-DD-YY", )

    ipms_cd45 = models.PositiveIntegerField(
        verbose_name="CD4 5",
        help_text="", )

    ipms_cd4date5 = models.DateField(
        verbose_name="CD4 5 date?",
        help_text="MM-DD-YY", )

    ipms_cd46 = models.PositiveIntegerField(
        verbose_name="CD4 6",
        help_text="", )

    ipms_cd4date6 = models.DateField(
        verbose_name="CD4 6 date?",
        help_text="MM-DD-YY", )

    ipms_cd47 = models.PositiveIntegerField(
        verbose_name="CD4 7",
        help_text="", )

    ipms_cd4date7 = models.DateField(
        verbose_name="CD4 7 date?",
        help_text="MM-DD-YY", )

    ipms_cd48 = models.PositiveIntegerField(
        verbose_name="CD4 8",
        help_text="", )

    ipms_cd4date8 = models.DateField(
        verbose_name="CD4 8 date?",
        help_text="MM-DD-YY", )

    ipms_cd49 = models.PositiveIntegerField(
        verbose_name="CD4 9",
        help_text="", )

    ipms_cd4date9 = models.DateField(
        verbose_name="CD4 9 date?",
        help_text="MM-DD-YY", )

    ipms_cd410 = models.PositiveIntegerField(
        verbose_name="CD4 10",
        help_text="", )

    ipms_cd4date10 = models.DateField(
        verbose_name="CD4 10 date?",
        help_text="MM-DD-YY", )

    ipms_cd411 = models.PositiveIntegerField(
        verbose_name="CD4 11",
        help_text="", )

    ipms_cd4date11 = models.DateField(
        verbose_name="CD4 11 date?",
        help_text="MM-DD-YY", )

    ipms_cd412 = models.PositiveIntegerField(
        verbose_name="CD4 12",
        help_text="", )

    ipms_cd4date12 = models.DateField(
        verbose_name="CD4 12 date?",
        help_text="MM-DD-YY", )

    ipms_cd413 = models.PositiveIntegerField(
        verbose_name="CD4 13",
        help_text="", )

    ipms_cd4date13 = models.DateField(
        verbose_name="CD4 13 date?",
        help_text="MM-DD-YY", )

    ipms_cd414 = models.PositiveIntegerField(
        verbose_name="CD4 14",
        help_text="", )

    ipms_cd4date14 = models.DateField(
        verbose_name="CD4 14 date?",
        help_text="MM-DD-YY", )

    ipms_cd415 = models.PositiveIntegerField(
        verbose_name="CD4 15",
        help_text="", )

    ipms_cd4date15 = models.DateField(
        verbose_name="CD4 15 date?",
        help_text="MM-DD-YY", )

    ipms_vlnum = models.PositiveIntegerField(
        verbose_name="How many Viral Loads are found in IPMS (before delivery)?",
        help_text="", )

    ipms_vl1 = models.CharField(
        verbose_name="Was Viral Load 1 (most recent):",
        max_length=1,
        choices=(('0', '<400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh1 = models.PositiveIntegerField(
        verbose_name="Viral Load 1 (value in copies/mL)",
        help_text="", )

    ipms_vldate1 = models.DateField(
        verbose_name="VL 1 date?",
        help_text="MM-DD-YY", )

    ipms_vl2 = models.CharField(
        verbose_name="Was Viral Load 2:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh2 = models.PositiveIntegerField(
        verbose_name="Viral Load 2 (value in copies/mL)",
        help_text="", )

    ipms_vldate2 = models.DateField(
        verbose_name="VL 2 date?",
        help_text="MM-DD-YY", )

    ipms_vl3 = models.CharField(
        verbose_name="Was Viral Load 3:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh3 = models.PositiveIntegerField(
        verbose_name="Viral Load 3 (value in copies/mL)",
        help_text="", )

    ipms_vldate3 = models.DateField(
        verbose_name="VL 3 date?",
        help_text="MM-DD-YY", )

    ipms_vl4 = models.CharField(
        verbose_name="Was Viral Load 4:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh4 = models.PositiveIntegerField(
        verbose_name="Viral Load 4 (value in copies/mL)",
        help_text="", )

    ipms_vldate4 = models.DateField(
        verbose_name="VL 4 date?",
        help_text="MM-DD-YY", )

    ipms_vl5 = models.CharField(
        verbose_name="Was Viral Load 5:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh5 = models.PositiveIntegerField(
        verbose_name="Viral Load 5 (value in copies/mL)",
        help_text="", )

    ipms_vldate5 = models.DateField(
        verbose_name="VL 5 date?",
        help_text="MM-DD-YY", )

    ipms_vl6 = models.CharField(
        verbose_name="Was Viral Load 6:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh6 = models.PositiveIntegerField(
        verbose_name="Viral Load 6 (value in copies/mL)",
        help_text="", )

    ipms_vldate6 = models.DateField(
        verbose_name="VL 6 date?",
        help_text="MM-DD-YY", )

    ipms_vl7 = models.CharField(
        verbose_name="Was Viral Load 7:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh7 = models.PositiveIntegerField(
        verbose_name="Viral Load 7 (value in copies/mL)",
        help_text="", )

    ipms_vldate7 = models.DateField(
        verbose_name="VL 7 date?",
        help_text="MM-DD-YY", )

    ipms_vl8 = models.CharField(
        verbose_name="Was Viral Load 8:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh8 = models.PositiveIntegerField(
        verbose_name="Viral Load 8 (value in copies/mL)",
        help_text="", )

    ipms_vldate8 = models.DateField(
        verbose_name="VL 8 date?",
        help_text="MM-DD-YY", )

    ipms_vl9 = models.CharField(
        verbose_name="Was Viral Load 9:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh9 = models.PositiveIntegerField(
        verbose_name="Viral Load 9 (value in copies/mL)",
        help_text="", )

    ipms_vldate9 = models.DateField(
        verbose_name="VL 9 date?",
        help_text="MM-DD-YY", )

    ipms_vl10 = models.CharField(
        verbose_name="Was Viral Load 10:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh10 = models.PositiveIntegerField(
        verbose_name="Viral Load 10 (value in copies/mL)",
        help_text="", )

    ipms_vldate10 = models.DateField(
        verbose_name="VL 10 date?",
        help_text="MM-DD-YY", )

    ipms_vl11 = models.CharField(
        verbose_name="Was Viral Load 11:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh11 = models.PositiveIntegerField(
        verbose_name="Viral Load 11 (value in copies/mL)",
        help_text="", )

    ipms_vldate11 = models.DateField(
        verbose_name="VL 11 date?",
        help_text="MM-DD-YY", )

    ipms_vl12 = models.CharField(
        verbose_name="Was Viral Load 12:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh12 = models.PositiveIntegerField(
        verbose_name="Viral Load 12 (value in copies/mL)",
        help_text="", )

    ipms_vldate12 = models.DateField(
        verbose_name="VL 12 date?",
        help_text="MM-DD-YY", )

    ipms_vl13 = models.CharField(
        verbose_name="Was Viral Load 13:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh13 = models.PositiveIntegerField(
        verbose_name="Viral Load 13 (value in copies/mL)",
        help_text="", )

    ipms_vldate13 = models.DateField(
        verbose_name="VL 13 date?",
        help_text="MM-DD-YY", )

    ipms_vl14 = models.CharField(
        verbose_name="Was Viral Load 14:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh14 = models.PositiveIntegerField(
        verbose_name="Viral Load 14 (value in copies/mL)",
        help_text="", )

    ipms_vldate14 = models.DateField(
        verbose_name="VL 14 date?",
        help_text="MM-DD-YY", )

    ipms_vl15 = models.CharField(
        verbose_name="Was Viral Load 15:",
        max_length=1,
        choices=(('0', '< 400 (undetectable)'), ('1', '>400 (not undetectable)')),
        help_text="", )

    ipms_vlhigh15 = models.PositiveIntegerField(
        verbose_name="Viral Load 15 (value in copies/mL)",
        help_text="", )

    ipms_vldate15 = models.DateField(
        verbose_name="VL 15 date?",
        help_text="MM-DD-YY", )

    ipms_priorart = models.CharField(
        verbose_name="Was any information on prior ART available in IPMS?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    ipms_prioartrsummary = models.TextField(
        verbose_name="Summarize Prior ART (include regimens, start dates, stop dates and reasons for starting and stopping)",
        help_text="", )

    ipms_syphilisnum = models.CharField(
        verbose_name="How many tests for syphilis (RPRs) during pregnancy are recorded in IPMS?",
        max_length=1,
        choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '>2')),
        help_text="", )

    ipms_syphdate1 = models.DateField(
        verbose_name="Date of most recent syphilis test (RPR) during pregnancy?",
        help_text="MM-DD-YY", )

    ipms_syphresult1 = models.CharField(
        verbose_name="Result of most recent syphilis test (RPR) in pregnancy?",
        max_length=1,
        choices=(('1', 'Reactive (positive)'), ('0', 'Non-reactive (negative)')),
        help_text="", )

    ipms_syphdate2 = models.DateField(
        verbose_name="Date of first syphilis test (RPR) during pregnancy?",
        help_text="MM-DD-YY", )

    ipms_syphresult2 = models.CharField(
        verbose_name="Result of first syphilis test (RPR) in pregnancy?",
        max_length=1,
        choices=(('1', 'Reactive (positive)'), ('0', 'Non-reactive (negative)')),
        help_text="", )

    ipms_cbcnum = models.CharField(
        verbose_name="How many Full Blood Counts (FBC) does this woman have during pregnancy (before delivery)?  **FBC includes WBC, Hb, Platelets, etc**",
        max_length=1,
        choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '>2')),
        help_text="", )

    imps_cbcdate1 = models.DateField(
        verbose_name="Date of the FBC during pregnancy 1  (most recent)",
        help_text="MM-DD-YY", )

    ipms_wbc1 = models.CharField(
        verbose_name="WBC count from FBC 1 in pregnancy (most recent)?",
        max_length=100,
        help_text="include 1 decimal place", )

    imps_hb1 = models.CharField(
        verbose_name="Hemoglobin (Hb) from FBC 1 during pregnancy (most recent)",
        max_length=100,
        help_text="include 1 decimal place", )

    imps_plt1 = models.PositiveIntegerField(
        verbose_name="Platelets (PLT) from FBC 1 in pregnancy (most recent)",
        help_text="whole number, no decimal place", )

    ipms_mcv1 = models.PositiveIntegerField(
        verbose_name="MCV from FBC 1 during pregnancy (most recent)",
        help_text="whole number, no decimal place", )

    imps_cbcdate2 = models.DateField(
        verbose_name="Date of the first FBC during pregnancy ",
        help_text="MM-DD-YY", )

    ipms_wbc2 = models.CharField(
        verbose_name="WBC count from the first FBC in pregnancy?",
        max_length=100,
        help_text="include 1 decimal place", )

    imps_hb2 = models.CharField(
        verbose_name="Hemoglobin (Hb) from the first FBC during pregnancy ",
        max_length=100,
        help_text="include 1 decimal place", )

    imps_plt2 = models.PositiveIntegerField(
        verbose_name="Platelets (PLT) from the first FBC in pregnancy ",
        help_text="whole number, no decimal place", )

    ipms_mcv2 = models.PositiveIntegerField(
        verbose_name="MCV from the first FBC during pregnancy ",
        help_text="whole number, no decimal place", )

    ipms_addinfo = models.TextField(
        verbose_name="Any addition information from IPMS",
        blank=True, null=True,
        help_text="", )

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'IPMS'
        verbose_name_plural = 'IPMS'
