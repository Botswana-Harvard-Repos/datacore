from django.db import models

from .model_mixins import CompleteFieldMixin, UuidModelMixin, RecordIDModelMixin


class OutcomesFour(UuidModelMixin, RecordIDModelMixin, CompleteFieldMixin, models.Model):

    mother_name = models.CharField(
        verbose_name="Mother's Name ",
        max_length=100,
        help_text="",
    )

    mother_omang = models.CharField(
        verbose_name="Mother's OMANG",
        max_length=100,
        blank=True,
        null=True,
        help_text="",
    )

    phone_number = models.CharField(
        verbose_name="Mother's Phone Number",
        max_length=100,
        blank=True,
        null=True,
        help_text="",
    )

    child_name = models.CharField(
        verbose_name="Child's Name ",
        max_length=100,
        blank=True,
        null=True,
        help_text="",
    )

    date_of_delivery = models.DateField(
        verbose_name="Date of Delivery (M-D-Y)",
        help_text="",
    )

    delivery_site = models.CharField(
        verbose_name="Delivery Site",
        max_length=2,
        choices=(
            ("10", "Princess Marina"),
            ("20", "Nyangabwge"),
            ("30", "Molepolole"),
            ("40", "Maun"),
            ("50", "Ghanzi"),
            ("60", "Selebi Phikwe"),
            ("70", "Serowe"),
            ("80", "Mahalapye"),
            ("90", "Bamalete Lutheran Hospital"),
            ("11", "Palapye Primary Hospital"),
            ("12", "Deborah Retief Hospaital"),
            ("13", "Kanye SDA Hospital"),
            ("14", "Athlone Hospital"),
            ("15", "Bobonong Primary Hospital"),
            ("16", "Gumare Primary Hospital"),
            ("17", "Goodhope Primary Hospital"),
            ("18", "Tutume Primary Hospital"),
            ("19", "Letlhakane Primary Hospital"),
        ),
        help_text="",
    )

    anc_clinic = models.CharField(
        verbose_name="ANC Clinic (Do NOT use abbreviations) ",
        max_length=100,
        blank=True,
        null=True,
        help_text="",
    )

    infant_status = models.CharField(
        verbose_name="Infant Status (at birth)",
        max_length=1,
        choices=(("1", "alive at discharge"), ("2", "unknown")),
        help_text="",
    )

    ca_diagnosis = models.CharField(
        verbose_name="Congenital Abnormality Diagnosis (at birth) ",
        max_length=100,
        blank=True,
        null=True,
        help_text="",
    )

    outcomes_consent = models.CharField(
        verbose_name="Did the mother consent to a follow-up call?",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        blank=True,
        null=True,
        help_text="",
    )

    overall_status = models.TextField(
        verbose_name="How are you doing? How is the child?",
        help_text="Please remember to ask about developmental milestones if child is alive",
    )

    child_status_phonecall = models.CharField(
        verbose_name="Child Current Status (per parent report)",
        max_length=1,
        choices=(("1", "alive"), ("2", "died")),
        help_text="",
    )

    cause_of_death = models.TextField(
        verbose_name="Circumstances of child death (including age, cause)",
        blank=True,
        null=True,
        help_text="",
    )

    services_childdeath = models.TextField(
        verbose_name="What type of care was the child receiving? (i.e. location (government or private), traditional medicine)",
        blank=True,
        null=True,
        help_text="",
    )

    parent_reported_diagnosis = models.CharField(
        verbose_name="Child's Diagnosis (per parent report)",
        max_length=100,
        help_text="",
    )

    diagnosis_explained = models.TextField(
        verbose_name="How was your infant's diagnosis and treatment explained to you? ",
        help_text="",
    )

    diagnosis_understood = models.CharField(
        verbose_name="Did you feel that you understood your infant's diagnosis?",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        help_text="",
    )

    diagnosis_questions = models.TextField(
        verbose_name="If no, what other questions do you still have? ",
        blank=True,
        null=True,
        help_text="",
    )

    prenatal_ultrasound = models.CharField(
        verbose_name="Did you receive a prenatal ultrasound that showed that your infant might be born with an abnormality?",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        blank=True,
        null=True,
        help_text="",
    )

    supports = models.TextField(
        verbose_name="What supports, if any, were available to you and your infant at the time of their birth? ",
        help_text="",
    )

    desired_supports = models.TextField(
        verbose_name="What supports would have been helpful for you? ",
        help_text="",
    )

    medical_intervention = models.CharField(
        verbose_name="Were you offered medical treatment to help your child? ",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        help_text="",
    )

    medical_tx_describe = models.TextField(
        verbose_name="If yes, please describe: ",
        blank=True,
        null=True,
        help_text="",
    )

    surgery = models.CharField(
        verbose_name="Did your child have surgery? ",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        help_text="",
    )

    surgery_details = models.TextField(
        verbose_name="If yes, please provide any additional details (i.e. what type of surgery, when was it, where was it done)",
        blank=True,
        null=True,
        help_text="",
    )

    ongoing_care = models.CharField(
        verbose_name="Is your child receiving any ongoing additional care (beyond routine care) because of their congenital abnormality/disability?  ",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        help_text="",
    )

    ongoing_care_describe = models.TextField(
        verbose_name="If yes, please describe ",
        blank=True,
        null=True,
        help_text="",
    )

    specialist_care = models.CharField(
        verbose_name="Does your child follow with a specialist (i.e. neurologist, orthopedics)? ",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        help_text="",
    )

    specialist_type = models.CharField(
        verbose_name="If yes, which specialist? ",
        max_length=100,
        blank=True,
        null=True,
        help_text="",
    )

    therapies = models.CharField(
        verbose_name="Were you offered additional therapies/services (i.e. physical or occupational therapy) to help your child? ",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        help_text="",
    )

    therapies_describe = models.TextField(
        verbose_name="If yes, please describe",
        blank=True,
        null=True,
        help_text="",
    )

    financial_services = models.CharField(
        verbose_name="Were you offered financial support to help deal with medical expenses related to your child's diagnosis? ",
        max_length=1,
        choices=(("1", "Yes"), ("0", "No")),
        help_text="",
    )

    financial_services_describe = models.TextField(
        verbose_name="If yes, please describe",
        blank=True,
        null=True,
        help_text="",
    )

    disability_social = models.TextField(
        verbose_name="What has been your experience in your community raising a child with a disability? ",
        help_text="",
    )

    questions_for_team = models.TextField(
        verbose_name="Are there any additional questions our team can help answer for you?",
        blank=True,
        null=True,
        help_text="",
    )

    imps_followup = models.TextField(
        verbose_name="IPMS/Records Follow-Up",
        blank=True,
        null=True,
        help_text="",
    )

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Outcomes 4'
        verbose_name_plural = 'Outcomes 4'
