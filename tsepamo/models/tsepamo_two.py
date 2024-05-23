from django.db import models

from .model_mixins import CompleteFieldMixin, UuidModelMixin, RecordIDModelMixin


class TsepamoTwo(UuidModelMixin, RecordIDModelMixin, CompleteFieldMixin, models.Model):

    site = models.CharField(
        verbose_name="Delivery Site",
        max_length=2,
        choices=(('1', 'PMH'), ('2', 'Nyangabgwe'), ('3', 'Molepolole'), ('4', 'Ghanzi'),
                 ('5', 'Maun'), ('6', 'Serowe'), ('7', 'Mahalapye'),
                 ('8', 'Selebi-Phikwe'), ('9', 'Bamalete Lutheran Hospital'),
                 ('10', 'Palapye Primary Hospital'), ('11', 'Deborah Retief Hospaital'),
                 ('12', 'Kanye SDA Hospital'), ('13', 'Athlone Hospital'),
                 ('14', 'Bobonong Primary Hospital'), ('15', 'Gumare Primary Hospital'),
                 ('16', 'Goodhope Primary Hospital'), ('17', 'Tutume Primary Hospital'),
                 ('18', 'Letlhakane Primary Hospital')),
        help_text="", )

    screen_cl = models.CharField(
        verbose_name="Was this woman SCREEENED for the cervical length study? (BLUE DOT ON MATERNITY CARD)",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    part_cl = models.CharField(
        verbose_name="Was this woman ENROLLED in the cervical length study?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    part_cl_bid = models.PositiveIntegerField(
        verbose_name="What is the cervical length study number?",
        help_text="Enter the 3 numbers AFTER CL-", )

    placental = models.CharField(
        verbose_name="Was this woman part of the placental sub-study?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    placenta_icsigned = models.CharField(
        verbose_name="Did this woman sign the Tsepamo Placental informed consent form version 1.0?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    placenta_dattimeconsent = models.DateTimeField(
        verbose_name="What was the date and time of the placental consent?",
        help_text="", )

    placenta_iccopy = models.CharField(
        verbose_name="Was this woman offered a copy of the placental informed consent for version 1.0?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    placenta_consent_received = models.CharField(
        verbose_name="Was consent received by the study coordinator?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    placenta_id = models.PositiveIntegerField(
        verbose_name="Placental ID: (this is the Tsepamo BID WITHOUT the first two numbers--site code (10))",
        help_text="", )

    placenta_hiv = models.CharField(
        verbose_name="What is the HIV status of the mother whose placenta was collected?",
        max_length=1,
        choices=(
            ('1', 'HIV-infected'), ('0', 'HIV-uninfected'), ('2', 'Unknown HIV status')),
        help_text="for placental participants only", )

    placenta_infantstat = models.CharField(
        verbose_name="What was the infant status?",
        max_length=1,
        choices=(('1', 'FSB/MSB'), ('0', 'live birth')),
        blank=True, null=True,
        help_text="for placental participants only", )

    placenta_nga = models.DecimalField(
        verbose_name="What was the gestational age at delivery?",
        decimal_places=2, max_digits=8,
        help_text="for placental participants only", )

    placenta_bwt = models.DecimalField(
        verbose_name="What was the birthweight?",
        decimal_places=2, max_digits=8,
        help_text="for placental participants only", )

    placenta_sga = models.DecimalField(
        verbose_name="Is this baby SGA?",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="1=YES BLANK=NO", )

    ntl_lab_date = models.DateField(
        verbose_name="What day was the placenta examined?",
        help_text="", )

    cord_frommarg = models.DecimalField(
        verbose_name="How far was the cord insertion from the margin?",
        decimal_places=2, max_digits=8,
        help_text="in cm", )

    cord_lngth = models.DecimalField(
        verbose_name="How long was the cord?",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="in cm", )

    cord_dm = models.DecimalField(
        verbose_name="What is the diameter of the cord?",
        decimal_places=2, max_digits=8,
        help_text="in cm", )

    cord_color = models.CharField(
        verbose_name="What is the color of the cord?",
        max_length=1,
        choices=(
        ('1', 'White'), ('2', 'Yellow'), ('3', 'Green'), ('4', 'Brown'), ('5', 'Other')),
        help_text="", )

    cord_color_other = models.TextField(
        verbose_name="Cord 'other' color, please specify:",
        help_text="", )

    placental_vessels = models.CharField(
        verbose_name="Number of vessels?",
        max_length=1,
        choices=(('1', '2'), ('2', '3'), ('3', 'unknown')),
        help_text="", )

    cord_twists = models.DecimalField(
        verbose_name="There are 3 twists in how many cm?",
        decimal_places=2, max_digits=8,
        help_text="", )

    cord_appear = models.CharField(
        verbose_name="Did the cord appear:",
        max_length=1,
        choices=(('1', 'Hypertwisted'), ('2', 'Flat'), ('3', 'None of the above')),
        help_text="", )

    trueknow = models.CharField(
        verbose_name="Did the cord have a true knot?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No'), ('2', 'Unknown')),
        help_text="", )

    cord_insert = models.CharField(
        verbose_name="Was the cord inserted into the:",
        max_length=1,
        choices=(('1', 'disk'), ('2', 'membrane'), ('3', 'unknown')),
        help_text="", )

    cord_otherfnd = models.TextField(
        verbose_name="other cord findings",
        blank=True, null=True,
        help_text="", )

    membrane_color = models.TextField(
        verbose_name="What is the membrane color?",
        help_text="", )

    membrane_otherfnd = models.TextField(
        verbose_name="Other membrane findings",
        blank=True, null=True,
        help_text="", )

    placenta_weight = models.DecimalField(
        verbose_name="What is the trimmed placental weight?",
        decimal_places=2, max_digits=8,
        help_text="in GM", )

    disc_diameter = models.DecimalField(
        verbose_name="What is the disc diameter?",
        decimal_places=2, max_digits=8,
        help_text="in cm", )

    disc_thick = models.DecimalField(
        verbose_name="How thick is the disc?",
        decimal_places=2, max_digits=8,
        help_text="in cm", )

    fetal_surf = models.TextField(
        verbose_name="Fetal surface findings?",
        blank=True, null=True,
        help_text="", )

    maternal_surf = models.TextField(
        verbose_name="Maternal surface findings?",
        blank=True, null=True,
        help_text="", )

    parench = models.TextField(
        verbose_name="Parenchyma findings?",
        blank=True, null=True,
        help_text="", )

    placenta_sectioned = models.CharField(
        verbose_name="Was the placenta examined and sectioned exactly as per protocol?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    not_protocol = models.TextField(
        verbose_name="Why wasn't the placenta examined or sectioned as per protocol?",
        help_text="", )

    slides_made = models.CharField(
        verbose_name="Were slides made of this placenta exactly as per protocol?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    noslides_reason = models.TextField(
        verbose_name="Why weren't slides made from this placenta?",
        help_text="", )

    placenta_boston = models.CharField(
        verbose_name="Were slides received in Boston?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    placental_bid = models.PositiveIntegerField(
        verbose_name="1.1 Placental ID",
        help_text="", )

    placenta_mature = models.CharField(
        verbose_name="1.2 Maturation",
        max_length=1,
        choices=(('1', 'Immature Placenta'), ('2', 'Mature Placenta'), ('3', 'Arrest'),
                 ('4', 'Distal villous hypoplasia')),
        help_text="", )

    placenta_parench = models.DecimalField(
        verbose_name="1.3 Parenchma-Number of Slides",
        decimal_places=2, max_digits=8,
        help_text="", )

    placenta_mroll = models.CharField(
        verbose_name="1.4 Membrane Roll",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_ucord = models.CharField(
        verbose_name="1.5 Umbilical Cord",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_basic_comment = models.TextField(
        verbose_name="Additional Comments--Basic Data",
        blank=True, null=True,
        help_text="", )

    placenta_dvasculo = models.CharField(
        verbose_name="2.1a Presence of Decidual Vasculopathy",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not Evaluable')),
        help_text="", )

    placenta_atherosis = models.CharField(
        verbose_name="2.1b Atherosis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not Evaluable')),
        help_text="", )

    placenta_distalvh = models.CharField(
        verbose_name="2.2 Distal Villous Hypoplasia",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Focal'), ('3', 'Patchy'), ('4', 'Multifocal'),
                 ('5', 'Diffuse')),
        help_text="", )

    placenta_infarct = models.CharField(
        verbose_name="2.3a Presence of Placental Infarcts",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_infarcttype = models.CharField(
        verbose_name="2.3b Type of infarct",
        max_length=1,
        choices=(('1', 'Usual type'), ('2', 'Hypertensive type'), ('3', 'Not evaluable')),
        help_text="", )

    placenta_usinfarctnum = models.DecimalField(
        verbose_name="2.3c Number of Usual Infarcts",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="", )

    placenta_htninfarctnum = models.DecimalField(
        verbose_name="2.3d Number of Hypertensive Infarcts",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="", )

    placenta_abruption = models.CharField(
        verbose_name="2.4a Presence of Abruption",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_abrupttype = models.CharField(
        verbose_name="2.4b Type of Abruption",
        max_length=1,
        choices=(('1', 'Chronic/Marginal'), ('2', 'Acute'), ('3', 'Subacute'),
                 ('4', 'Inflammatory'), ('5', 'Not Evaluable')),
        help_text="", )

    placental_synknot = models.CharField(
        verbose_name="2.5 Increased Syncytial Knotting",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Focal'), ('3', 'Patchy'), ('4', 'Multifocal'),
                 ('5', 'Diffuse')),
        help_text="", )

    placenta_cysts = models.CharField(
        verbose_name="2.6 Chorionic Microcysts",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not evaluable')),
        help_text="", )

    placenta_necrosis = models.CharField(
        verbose_name="2.7 Chorionic/Decidual Laminar Necrosis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not evaluable')),
        help_text="", )

    placenta_perfusion_other = models.TextField(
        verbose_name="2.8 Maternal Vascular Malperfusion -- Other",
        blank=True, null=True,
        help_text="", )

    placenta_fetalmalp = models.CharField(
        verbose_name="3.1a Fetal Vascular Malperfusion",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_fetalmal_grade = models.CharField(
        verbose_name="3.1b Grade - Fetal Vascular Malperfusion",
        max_length=1,
        choices=(('1', 'Low Grade'), ('2', 'High Grade'), ('3', 'Not evaluable')),
        help_text="", )

    placenta_vsk = models.CharField(
        verbose_name="3.2 Villous Stromal Karyorrhexis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not Evaluable')),
        help_text="", )

    placenta_avascvilli = models.CharField(
        verbose_name="3.3 Avascular Villi",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not Evaluable')),
        help_text="", )

    placenta_largethrombus = models.CharField(
        verbose_name="3.4 Large Vessel Thrombus",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not Evaluable')),
        help_text="", )

    placenta_fetalmal_comment = models.TextField(
        verbose_name="3.5 Fetal Vascular Malperfusion--Other",
        blank=True, null=True,
        help_text="", )

    placenta_villitis = models.CharField(
        verbose_name="4.1a Presence of Chronic Villitis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_spvillitis = models.CharField(
        verbose_name="4.2a Specific Villitis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_organism = models.TextField(
        verbose_name="4.2b Specific Organism",
        blank=True, null=True,
        help_text="", )

    placenta_villitisunk = models.CharField(
        verbose_name="4.3 Villitis of Unknown Etiology",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_grade_villitisunk = models.CharField(
        verbose_name="4.3b Grade Villitis of Unknown Etiology",
        max_length=1,
        choices=(('1', 'Low Grade'), ('2', 'High Grade')),
        help_text="", )

    placenta_deciduitis = models.CharField(
        verbose_name="4.4 Deciduitis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_necdecid = models.CharField(
        verbose_name="4.4b Necrotizing Deciduitis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not Evaluable')),
        blank=True, null=True,
        help_text="", )

    placenta_pcdecid = models.CharField(
        verbose_name="4.4c Plasma Cell Deciduitis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present'), ('3', 'Not evaluable')),
        blank=True, null=True,
        help_text="", )

    placenta_chorio = models.CharField(
        verbose_name="4.5 Acute Chorioamnionitis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_matstage = models.CharField(
        verbose_name="4.5b Maternal Stage",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Stage 1'), ('3', 'Stage 2'), ('4', 'Stage 3')),
        help_text="", )

    placenta_matgrade = models.CharField(
        verbose_name="4.5c Maternal Grade",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Grade 1'), ('3', 'Grade 2')),
        help_text="", )

    placenta_fetstage = models.CharField(
        verbose_name="4.5d Fetal Stage",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Stage 1'), ('3', 'Stage 2'), ('4', 'Stage 3')),
        help_text="", )

    placenta_fetgrade = models.CharField(
        verbose_name="4.5e Fetal Grade",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Grade 1'), ('3', 'Grade 2')),
        help_text="", )

    placenta_malaria = models.CharField(
        verbose_name="4.6a Presence of Malaria",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_malariachar = models.CharField(
        verbose_name="4.6b Malaria Characteristics",
        max_length=1,
        choices=(
        ('1', 'sequestration'), ('2', 'pigment'), ('3', 'congenital'), ('4', 'Acute'),
        ('5', 'Not evaluable')),
        help_text="", )

    placenta_inflammpath_other = models.TextField(
        verbose_name="4.7 Inflammatory Pathology--Other",
        blank=True, null=True,
        help_text="", )

    placenta_edema = models.CharField(
        verbose_name="5.1 Edema",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_meconium = models.CharField(
        verbose_name="5.2 Meconium",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_sickled = models.CharField(
        verbose_name="5.3 Sickled Maternal RBCs",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_ivthrombi = models.CharField(
        verbose_name="5.4 Intervillous Thrombi",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Present')),
        help_text="", )

    placenta_chorangiosis = models.CharField(
        verbose_name="5.5 Chorangiosis",
        max_length=1,
        choices=(('1', 'Absent'), ('2', 'Focal'), ('3', 'Patchy'), ('4', 'Multifocal'),
                 ('5', 'Diffuse')),
        help_text="", )

    placenta_otherpathology = models.TextField(
        verbose_name="5.6 Other",
        blank=True, null=True,
        help_text="", )

    placental_pathdesc = models.TextField(
        verbose_name="What were the pathologist's findings?",
        help_text="", )

    placental_diagnosis = models.CharField(
        verbose_name="What is the histopathologic diagnosis?",
        max_length=1,
        choices=(('1', 'Normal'),
                 ('2', '2 XXX (this question is requires further input from Drucilla)')),
        help_text="", )

    cardavailable = models.CharField(
        verbose_name="Is the Maternity Card Available?  (answer NO only if the maternity card is lost, missing, or was never brought in by the mother.  If only part of the maternity card is ripped out, please answer YES)",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    nonbooker = models.CharField(
        verbose_name="Non-Booker?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    ancreg = models.CharField(
        verbose_name="ANC Registration Clinic (Do NOT use Abbreviations)",
        max_length=100,
        help_text="If not known, write UNKNOWN.", )

    cliniccode = models.PositiveIntegerField(
        verbose_name="ANC Registration Clinic Code (5-digits)",
        blank=True, null=True,
        help_text="If clinic code is not found, please enter 88888", )

    bookdate = models.DateField(
        verbose_name="Booking Date at ANC",
        blank=True, null=True,
        help_text="MM - DD - YY If UNKNOWN, Leave BLANK", )

    bookdateunknown = models.CharField(
        verbose_name="Is ANC booking date unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    matage = models.PositiveIntegerField(
        verbose_name="Maternal Age",
        blank=True, null=True,
        help_text="If Maternal age unknown, LEAVE BLANK", )

    matageunknown = models.CharField(
        verbose_name="Is Maternal Age Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    maritalstat = models.CharField(
        verbose_name="Marital Status:",
        max_length=2,
        choices=(('1', 'Single'), ('2', 'Married'), ('3', 'Widowed'), ('4', 'Divorced'),
                 ('99', 'UNKNOWN')),
        help_text="", )

    national = models.CharField(
        verbose_name="Nationality:",
        max_length=2,
        choices=(
        ('99', 'UNKNOWN'), ('1', 'Motswana'), ('2', 'Zimbabwean'), ('3', 'Kenyan'),
        ('4', 'South African'), ('5', 'Chinese'), ('6', 'Indian'), ('7', 'Congolese'),
        ('8', 'Lesotho'), ('9', 'Malawi'), ('10', 'Zambia'), ('11', 'Tanzania'),
        ('12', 'Nigeria'), ('13', 'Other'), ('14', 'Pakistani'), ('15', 'Bangladesh'),
        ('16', 'Ghana'), ('17', 'Guineean'), ('18', 'Ugandan'), ('19', 'Somalian'),
        ('20', 'Sierra Leone'), ('21', 'Non-citizen (but not specified)'),
        ('22', 'Namibian'), ('23', 'Ethiopian')),
        help_text="", )

    nationalother = models.TextField(
        verbose_name="Other Nationality, Specify:",
        help_text="", )

    educ = models.CharField(
        verbose_name="Education:",
        max_length=2,
        choices=(('1', 'Standard/Primary'), ('2', 'Secondary or Equivalent'),
                 ('3', 'Tertiary or University'), ('4', 'None'), ('99', 'Unknown')),
        help_text="", )

    occup = models.CharField(
        verbose_name="Occupation:",
        max_length=2,
        choices=(('1', 'Student'), ('2', 'Housewife or None'), ('3', 'Salaried'),
                 ('99', 'Unknown')),
        help_text="", )

    grav = models.PositiveIntegerField(
        verbose_name="Gravida",
        blank=True, null=True,
        help_text="If gravida is not known, LEAVE BLANK", )

    gravmissing = models.CharField(
        verbose_name="Is Gravida Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    para = models.PositiveIntegerField(
        verbose_name="Para",
        blank=True, null=True,
        help_text="If para is missing, please LEAVE BLANK", )

    paramissing = models.CharField(
        verbose_name="Is Para Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    hx_preterm = models.CharField(
        verbose_name="History of Preterm Delivery (36 weeks or Less) in previous pregnancies?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    hx_stillbirth = models.CharField(
        verbose_name="History of Stillbirth (FSB/MSB) in previous pregnancies?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    admit_pregnancy = models.CharField(
        verbose_name="Was the patient admitted during this pregnancy and discharged before delivery?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="Admissions only PRIOR to admission for labor and delivery", )

    number_admit_pregnancy = models.CharField(
        verbose_name="How many times was the patient admitted during this pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 or more')),
        help_text="", )

    date_admit1_pregnancy = models.DateField(
        verbose_name="What was the date of the first admission?",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    date_admit1_unknown = models.CharField(
        verbose_name="Was the date of first admission UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    admit1_diag = models.TextField(
        verbose_name="What was the Diagnosis during the first admission?",
        help_text="If UNKNOWN, write UNKNOWN", )

    date_admit2_pregnancy = models.DateField(
        verbose_name="What was the date of the second admission?",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    date_admit2_unknown = models.CharField(
        verbose_name="Was the date of second admission UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        blank=True, null=True,
        help_text="", )

    admit2_diag = models.TextField(
        verbose_name="What was the Diagnosis during the second admission?",
        help_text="If UNKNOWN, write UNKNOWN", )

    date_admit3_pregnancy = models.DateField(
        verbose_name="What was the date of the third admission?",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    date_admit3_unknown = models.CharField(
        verbose_name="Was the date of third admission UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    admit3_diag = models.TextField(
        verbose_name="What was the Diagnosis during the third admission?",
        help_text="If UNKNOWN, write UNKNOWN", )

    date_admit4_pregnancy = models.DateField(
        verbose_name="What was the date of the fourth admission?",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    date_admit4_unknown = models.CharField(
        verbose_name="Was the date of fourth admission UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    admit4_diag = models.TextField(
        verbose_name="What was the Diagnosis during the fourth admission?",
        help_text="If UNKNOWN, write UNKNOWN", )

    date_admit5_pregnancy = models.DateField(
        verbose_name="What was the date of the fifth admission?",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    date_admit5_unknown = models.CharField(
        verbose_name="Was the date of fifth admission UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    admit5_diag = models.TextField(
        verbose_name="What was the Diagnosis during the fifth admission?",
        help_text="If UNKNOWN, write UNKNOWN", )

    anymedhist = models.CharField(
        verbose_name="Medical History BEFORE PREGNANCY:",
        max_length=2,
        choices=(
        ('1', 'Cardiac'), ('2', 'Renal'), ('3', 'STD'), ('4', 'TB'), ('5', 'Diabetes'),
        ('6', 'Epilepsy'), ('7', 'Anemia'), ('8',
                                             'High BP (hypertension, high blood pressure, elevated BP but NOT PIH or Gestational Hypertension)'),
        ('15', 'PIH/Gestational Hypertension'), ('18', 'Pre-eclampsia/Eclampsia'),
        ('9', 'Hypothyroidism'), ('10', 'Asthma'), ('11', 'Cancer'),
        ('12', 'Psychiatric Illness'), ('13', 'Other'),
        ('14', 'ulcer/abdominal ulcer/peptic ulcer/gastritis'),
        ('16', 'Migraine/severe headache'), ('17', 'DVT (Deep Vein Thrombosis)'),
        ('19', 'Genital warts/warts'), ('20', 'Fibroids/fibroid uterus'),
        ('21', 'Backache/Waist ache/ chronic back pain'), ('0', 'NONE'),
        ('99', 'UNKNOWN')),
        help_text="Check All that Apply", )

    othermedhistsp = models.CharField(
        verbose_name="Medical History Other, Specify:",
        max_length=100,
        help_text="", )

    specify_cancer = models.TextField(
        verbose_name="Specify Type of Cancer if known:",
        help_text="If UNKNOWN, write UNKNOWN", )

    tbhist_currenttreat = models.CharField(
        verbose_name="Was this woman on anti-TB medication at any time during THIS pregnancy?",
        max_length=1,
        choices=(
        ('1', 'Yes'), ('0', 'No (TB treated BEFORE this pregnancy or not documented)')),
        help_text="", )

    highbpmed = models.CharField(
        verbose_name="Which Blood Pressure medication was she on PRIOR to pregnancy?",
        max_length=2,
        choices=(('1', 'Methyldopa'), ('2', 'Nifedipine'), ('3', 'Hydralazine'),
                 ('4', 'Hydrochlorothiazide (HCTZ)'), ('5', 'Enalapril'),
                 ('6', 'Captopril'), ('7', 'Atenolol'), ('9', 'Propranolol'),
                 ('10', 'Carvedilol'), ('11', 'Unspecified antihypertensive medication'),
                 ('8', 'Other'), ('0', 'NONE'), ('99', 'UNKNOWN')),
        help_text="Check All that Apply", )

    highbpmedother = models.TextField(
        verbose_name="If other BP med, specify:",
        help_text="", )

    methydopa_cont = models.CharField(
        verbose_name="Was Methyldopa continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    nifedipine_cont = models.CharField(
        verbose_name="Was Nifedipine continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    hydralazine_cont = models.CharField(
        verbose_name="Was Hydralazine continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    hctz_cont = models.CharField(
        verbose_name="Was Hydrochlorothiazide (HCTZ) continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    enalapril_cont = models.CharField(
        verbose_name="Was Enalapril continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    captopril_cont = models.CharField(
        verbose_name="Was Captopril continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    atenolol_cont = models.CharField(
        verbose_name="Was Atenolol continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    otherbpmed_cont = models.CharField(
        verbose_name="Was Other BP Medication continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    epilepsymed = models.CharField(
        verbose_name="Which Epilepsy medication was she on prior to pregnancy?",
        max_length=2,
        choices=(('1', 'Valproate'), ('2', 'Carbemazapine'), ('3', 'Phenytoin'),
                 ('4', 'Phenobarbitol'), ('5', 'Other'), ('0', 'NONE'),
                 ('99', 'UNKNOWN')),
        help_text="Check All that Apply", )

    epilepsymedother = models.CharField(
        verbose_name="If other Epilepsy Med, Specify:",
        max_length=100,
        help_text="", )

    valproate_cont = models.CharField(
        verbose_name="Was Valproate continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    carbemaz_cont = models.CharField(
        verbose_name="Was Carbemazapime continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    phenytoin_cont = models.CharField(
        verbose_name="Was Phenytoin continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    phenobarb_cont = models.CharField(
        verbose_name="Was Phenobarbital continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    otheraed_cont = models.CharField(
        verbose_name="Was Other Epilepsy Medication continued DURING this pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    alcohol = models.CharField(
        verbose_name="Other Risks: Alcohol during this pregnancy",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    smoking = models.CharField(
        verbose_name="Other Risks: Smoking during this pregnancy",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    firsthb = models.CharField(
        verbose_name="Haemoglobin (Hb) First visit:",
        max_length=100,
        blank=True, null=True,
        help_text="If Hb is unknown, LEAVE BLANK. Must use 1 decimal point (eg. 10.0)", )

    firsthbunknown = models.CharField(
        verbose_name="Is the first Hb UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    hb_date = models.DateField(
        verbose_name="First Hb Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    firsthb_dateunknown = models.CharField(
        verbose_name="Is the first Hb DATE UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    firstrpr = models.CharField(
        verbose_name="First VDRL/RPR",
        max_length=2,
        choices=(('1', 'Positive (Reactive)'), ('0', 'Negative (Non-Reactive/NR)'),
                 ('99', 'UNKNOWN')),
        help_text="", )

    rpr1_date = models.DateField(
        verbose_name="First VDRL/RPR Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    rpr1_dateunknown = models.CharField(
        verbose_name="Is the first VDRL/RPR DATE UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    blood = models.CharField(
        verbose_name="Blood Group",
        max_length=2,
        choices=(('1', 'A'), ('2', 'B'), ('3', 'O'), ('4', 'AB'), ('99', 'UNKNOWN')),
        help_text="", )

    rh = models.CharField(
        verbose_name="Rh Factor",
        max_length=2,
        choices=(('1', 'Positive'), ('0', 'Negative'), ('99', 'UNKNOWN')),
        help_text="", )

    secondhb = models.CharField(
        verbose_name="2nd Haemoglobin (Hb) :",
        max_length=100,
        blank=True, null=True,
        help_text="If Hb is unknown, LEAVE BLANK. Must use 1 decimal point (eg. 10.0)", )

    secondhbunknown = models.CharField(
        verbose_name="Is second Hb UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    hb2_date = models.DateField(
        verbose_name="Second Hb DATE",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    secondhb_dateunknown = models.CharField(
        verbose_name="Is the second Hb DATE UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    lastrpr = models.CharField(
        verbose_name="RPR VDRL (34-36)",
        max_length=2,
        choices=(('1', 'Positive (Reactive)'), ('0', 'Negative (Non-Reactive/NR)'),
                 ('99', 'Unknown')),
        blank=True, null=True,
        help_text="", )

    rpr2_date = models.DateField(
        verbose_name="RPR/VDRL 34-36 wks Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    rpr2_dateunknown = models.CharField(
        verbose_name="Is the RPR VDRL 34-36wks DATE UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    mps = models.CharField(
        verbose_name="Is there documentation of ANY MPS (malaria parasite smear?)",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    mps_number = models.CharField(
        verbose_name="How many MPS results are recorded?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3')),
        help_text="", )

    mps1_date = models.DateField(
        verbose_name="What is the date of the 1st visit MPS?",
        blank=True, null=True,
        help_text="If date is missing, LEAVE BLANK", )

    mps1_result = models.CharField(
        verbose_name="What is the result of the 1st visit MPS?",
        max_length=2,
        choices=(('1', 'Positive'), ('0', 'Negative'), ('99', 'Unknown')),
        blank=True, null=True,
        help_text="", )

    mps2_date = models.DateField(
        verbose_name="What is the date of the 20-24week MPS?",
        blank=True, null=True,
        help_text="If date is missing, LEAVE BLANK", )

    mps2_result = models.CharField(
        verbose_name="What is the result of the 20-24week MPS?",
        max_length=2,
        choices=(('1', 'Positive'), ('0', 'Negative'), ('99', 'Unknown')),
        blank=True, null=True,
        help_text="", )

    mps3_date = models.DateField(
        verbose_name="What is the date of the 34-36 week MPS?",
        blank=True, null=True,
        help_text="If date is missing, LEAVE BLANK", )

    mps3_result = models.CharField(
        verbose_name="What is the result of the 34-36week MPS?",
        max_length=2,
        choices=(('1', 'Positive'), ('0', 'Negative'), ('99', 'Unknown')),
        blank=True, null=True,
        help_text="", )

    hivpos = models.CharField(
        verbose_name="HIV positive?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('2', 'Declined'), ('99', 'UNKNOWN')),
        help_text="", )

    hivform_available = models.CharField(
        verbose_name="Is the HIV data abstraction form available?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="This refers to the half-page abstracted form where HIV information has been confirmed ", )

    nohivform_reason = models.CharField(
        verbose_name="Why was the data abstraction form not available?",
        max_length=1,
        choices=(('1', 'Participant not approached because of  weekend/holiday'), ('2',
                                                                                   'Participant not approached because she was transferred to another hospital or to a clinic'),
                 ('3',
                  'Participant not approached because she was too ill to answer questions'),
                 ('4', 'Participant refused to answer questions'),
                 ('5', 'Form was filled but lost'), ('6', 'Other'), ('7', 'Unknown')),
        help_text="", )

    nohivform_reasonother = models.TextField(
        verbose_name="Other Reason for not completing HIV abstraction form, specify",
        help_text="", )

    idcccard_available = models.CharField(
        verbose_name="Was the IDCC card used to fill in the HIV abstraction form?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="If IDCC was used to fill in any of the information in the HIV abstraction form, choose YES", )

    hivform_summary = models.TextField(
        verbose_name="\"Please summarize the ART history in the HIV abstraction form. Please include 1. All ART regimens ever taken2. The dates ART regimens started and stopped 3. The reasons for starting and stopping\"",
        blank=True, null=True,
        help_text="", )

    summary_reviewed = models.CharField(
        verbose_name="Did Judith review the summary? (Only Judith should answer this question, RA should leave this blank)",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    timingtest = models.CharField(
        verbose_name="Timing of the positive test",
        max_length=2,
        choices=(('1', 'Known to be HIV+ prior to current pregnancy'),
                 ('2', 'Current pregnancy tested HIV+ for the first time'),
                 ('3', 'HIV positive test first determined after delivery'),
                 ('99', 'UNKNOWN')),
        help_text="", )

    timingtest_source = models.CharField(
        verbose_name="For timing of test: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB record')),
        help_text="All answers chosen must AGREE", )

    numbertests = models.CharField(
        verbose_name="How many total HIV tests during pregnancy (including at maternity)?",
        max_length=1,
        choices=(('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five'),
                 ('6', 'Six')),
        help_text="", )

    date_firsttest = models.DateField(
        verbose_name="Date of first HIV test in pregnancy?",
        blank=True, null=True,
        help_text="MM-DD-YY If Unknown, leave blank", )

    firsttest_unk = models.CharField(
        verbose_name="Is the date of first HIV test in pregnancy unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    result_firsttest = models.CharField(
        verbose_name="What was the result of the first HIV test in pregnancy?",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminant')),
        help_text="", )

    date_secondtest = models.DateField(
        verbose_name="Date of second HIV test in pregnancy?",
        blank=True, null=True,
        help_text="MM-DD-YY If Unknown, leave blank", )

    secondtest_unk = models.CharField(
        verbose_name="Is the date of second HIV test in pregnancy unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    result_secondtest = models.CharField(
        verbose_name="What was the result of the second HIV test in pregnancy?",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminant')),
        help_text="", )

    date_thirdtest = models.DateField(
        verbose_name="Date of third HIV test in pregnancy?",
        blank=True, null=True,
        help_text="MM-DD-YY If Unknown, leave blank", )

    thirdtest_unk = models.CharField(
        verbose_name="Is the date of third HIV test in pregnancy unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    result_thirdtest = models.CharField(
        verbose_name="What was the result of the third HIV test in pregnancy?",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminant')),
        help_text="", )

    date_fourthtest = models.DateField(
        verbose_name="Date of fourth HIV test in pregnancy?",
        blank=True, null=True,
        help_text="MM-DD-YY If Unknown, leave blank", )

    fourthtest_unk = models.CharField(
        verbose_name="Is the date of fourth HIV test in pregnancy unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    result_fourthtest = models.CharField(
        verbose_name="What was the result of the fourth HIV test in pregnancy?",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminant')),
        help_text="", )

    date_fifthtest = models.DateField(
        verbose_name="Date of fifth HIV test in pregnancy?",
        blank=True, null=True,
        help_text="MM-DD-YY If Unknown, leave blank", )

    fifthtest_unk = models.CharField(
        verbose_name="Is the date of fifth HIV test in pregnancy unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    result_fifthtest = models.CharField(
        verbose_name="What was the result of the fifth HIV test in pregnancy?",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminant')),
        help_text="", )

    date_sixthtest = models.DateField(
        verbose_name="Date of sixth HIV test in pregnancy?",
        blank=True, null=True,
        help_text="MM-DD-YY If Unknown, leave blank", )

    sixthtest_unk = models.CharField(
        verbose_name="Is the date of sixth HIV test in pregnancy unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    result_sixtest = models.CharField(
        verbose_name="What was the result of the sixth HIV test in pregnancy?",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminant')),
        help_text="", )

    datediagnosis = models.DateField(
        verbose_name="Date first tested positive (date of HIV diagnosis)",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    datediagnosisunknown = models.CharField(
        verbose_name="Is Date of first positive test UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    datediagnosisest = models.CharField(
        verbose_name="Is any part of this date estimated?",
        max_length=1,
        choices=(('1', 'Day'), ('2', 'Month'), ('3', 'NONE'),
                 ('4', 'Not Applicable (Diagnosis Date Unknown)')),
        help_text="Check All that Apply", )

    datediagnosis_source = models.CharField(
        verbose_name="For date of HIV diagnosis: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB record')),
        help_text="All answers chosen must AGREE (have the same information)", )

    counseledonfeeding = models.CharField(
        verbose_name="Was counseling on infant feeding provided during pregnancy or after delivery?",
        max_length=1,
        choices=(('1', 'Yes'), ('2', 'No (documented that no counseling provided)'),
                 ('3', 'Unknown (not documented)')),
        blank=True, null=True,
        help_text="", )

    feedingcounselingdate = models.DateField(
        verbose_name="Date of feeding counseling?",
        blank=True, null=True,
        help_text="MM-DD-YY  If UNKNOWN, leave blank", )

    counseldateunknown = models.CharField(
        verbose_name="Is Date of feeding counseling UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        blank=True, null=True,
        help_text="", )

    plannedfeeding = models.CharField(
        verbose_name="What is the planned method of infant feeding?",
        max_length=1,
        choices=(('1', 'Breastfeeding (BF or EBF)'), ('2', 'Formula feeding (FF or EFF)'),
                 ('3', 'Undecided'), ('4', 'Unknown (not recorded)')),
        blank=True, null=True,
        help_text="", )

    cd4_prior = models.CharField(
        verbose_name="Are there any CD4 counts available PRIOR to pregnancy",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="Please answer NO if results from prior CD4 testing are not available", )

    nadircd4_count = models.DecimalField(
        verbose_name="What is the LOWEST CD4 count recorded PRIOR to pregnancy?",
        decimal_places=2, max_digits=8,
        help_text="", )

    nadircd4_date = models.DateField(
        verbose_name="What is the date of the LOWEST CD4 count recorded PRIOR to pregnancy?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    nadircd4_dateunknown = models.CharField(
        verbose_name="Is the date of the LOWEST CD4 count PRIOR to pregnancy unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    cd4 = models.CharField(
        verbose_name="Is CD4 count reported or documented as drawn DURING PREGNANCY?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    cd4_source = models.CharField(
        verbose_name="Is CD4 reported/documented as drawn: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB record')),
        help_text="All answers chosen must AGREE (have the same information)", )

    cd4s_during = models.CharField(
        verbose_name="How many CD4 counts are documented to have been drawn DURING pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3 or more')),
        help_text="", )

    cd4_during_source = models.CharField(
        verbose_name="The number of CD4s in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB record')),
        help_text="All answers chosen must AGREE (have the same information)", )

    recent_cd4 = models.PositiveIntegerField(
        verbose_name="First CD4 count during pregnancy:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    recentcd4unknown = models.CharField(
        verbose_name="Is the first CD4 count drawn in pregnancy UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    recent_cd4_source = models.CharField(
        verbose_name="For the first CD4 in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    datecd4 = models.DateField(
        verbose_name="Date of the first CD4 count drawn in pregnancy?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    datecd4unknown = models.CharField(
        verbose_name="Is the date of the first CD4 count in pregnancy UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    datecd4_source = models.CharField(
        verbose_name="For the date of the first CD4 in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB Card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    second_cd4 = models.PositiveIntegerField(
        verbose_name="Second CD4 count during pregnancy:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    secondcd4unknown = models.CharField(
        verbose_name="Is the second CD4 count drawn in pregnancy UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    secondcd4_source = models.CharField(
        verbose_name="For the second CD4 in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    datesecondcd4 = models.DateField(
        verbose_name="Date of the second CD4 count drawn in pregnancy?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    datesecondcd4unknown = models.CharField(
        verbose_name="Is the date of the second CD4 count in pregnancy UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    datesecondcd4_source = models.CharField(
        verbose_name="For the date of the second CD4 in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    third_cd4 = models.PositiveIntegerField(
        verbose_name="Third CD4 count during pregnancy:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    thirdcd4unknown = models.CharField(
        verbose_name="Is the third CD4 count drawn in pregnancy UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    thirdcd4_source = models.CharField(
        verbose_name="For the third CD4 in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="", )

    datethirdcd4 = models.DateField(
        verbose_name="Date of the third CD4 count drawn in pregnancy?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    datethirdcd4unknown = models.CharField(
        verbose_name="Is the date of the third CD4 count in pregnancy UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    datethirdcd4_source = models.CharField(
        verbose_name="For the date of the third CD4 in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    viral_load = models.CharField(
        verbose_name="Is there documentation of an HIV viral load drawn DURING PREGNANCY",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    viral_load_source = models.CharField(
        verbose_name="For documentation of viral load in pregnancy: Source of information used in the HIV abstraction form? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    vl_number = models.CharField(
        verbose_name="How many viral loads are documented during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    vl_number_source = models.CharField(
        verbose_name="For how many viral loads in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    vl1_undetect = models.CharField(
        verbose_name="Is the first viral load undetectable (< 400 or less than 400)? ",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="If the viral load is higher than 400, choose NO", )

    high_vl = models.PositiveIntegerField(
        verbose_name="What is the first viral load during pregnancy?",
        help_text="", )

    vl1_source = models.CharField(
        verbose_name="For value of first viral load in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB Card')),
        help_text="", )

    vl1_date = models.DateField(
        verbose_name="What is the date of the first viral load in pregnancy?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    vl1_dateunknown = models.CharField(
        verbose_name="Is the date of the first viral load drawn in pregnancy unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    vl1date_source = models.CharField(
        verbose_name="For date of first viral load in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    vl2_undetect = models.CharField(
        verbose_name="Is the second viral load undetectable (<400)?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    high_vl2 = models.PositiveIntegerField(
        verbose_name="What is the second viral load during pregnancy?",
        help_text="", )

    vl2_source = models.CharField(
        verbose_name="For value of second viral load in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    vl2_date = models.DateField(
        verbose_name="What is the date of the second viral load in pregnancy?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    vl2_dateunknown = models.CharField(
        verbose_name="Is the date of the second viral load drawn in pregnancy unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    vl2date_source = models.CharField(
        verbose_name="For date of second viral load in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    anyarvs = models.CharField(
        verbose_name="Is there documentation of ANY ARVs initiated or continued during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    preg_adherence = models.CharField(
        verbose_name="Missed more than 3 days of ART during this pregnancy? (since starting ART)",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    hivform_default = models.CharField(
        verbose_name="During pregnancy has the mom defaulted from treatment and then restarted treatment? ",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    hivform_defaultsummary = models.TextField(
        verbose_name="Please write a summary of defaulting: -include the regimen the woman was on when she defaulted and the regimen that was restarted-include the dates of stopping and restarting",
        help_text="", )

    preg_adherence_source = models.CharField(
        verbose_name="For missed ART in pregnancy: Source of information used in the HIV abstraction form? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    conceptarv = models.CharField(
        verbose_name="Is there documentation of ART at the time of CONCEPTION?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    conceptarv_source = models.CharField(
        verbose_name="For ART at conception: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    initialreg = models.CharField(
        verbose_name="Initial Regimen prescribed or continued during pregnancy?For those starting during pregnancy: the first regimen they startedFor those on ART prior to conception: the regimen that they were on when they got pregnant with THIS pregnancy (regimen at conception for this birth)",
        max_length=2,
        choices=(
        ('1', 'AZT only'), ('2', 'Atripla (or TDF/FTC/EFV or TRU/EFV or Atroiza)'),
        ('21', 'TDF/FTC/DTG (or TRU/DTG)(or TRU/Dolutegravir)'),
        ('30', 'TDF/3TC/DTG (or TLD or DLT or TDF/3TC/Dolutegravir)'), ('32',
                                                                        'TAF-ED (or TAF/FTC/DTG or Tenofovir Alafenamide/emtricitabine/dolutegravir)'),
        ('29', 'EFV/D4T/3TC'), ('3', 'NVP/CBV (or NVP/AZT/3TC)'),
        ('4', 'ALU/CBV (or ALU/AZT/3TC or LPV/rit/AZT/3TC)'), ('5', 'NVP/D4T/3TC'),
        ('6', 'ALU/D4T/3TC (or LPV/rit/D4T/3TC)'), ('7', 'NVP/TRU (or NVP/TDF/FTC)'),
        ('8', 'ALU/TRU (or ALU/TDF/FTC or LPV/rit/TDF/FTC)'),
        ('9', 'EFV/CBV (or EFV/AZT/3TC)'), ('10', 'EFV/TRU'),
        ('26', 'ABC/3TC/DTG (Abacavir/3TC/Dolutegravir)'), ('11', 'ABC/3TC/NVP'),
        ('12', 'ABC/3TC/LPV/rit'), ('13', 'ABC/3TC/EFV'),
        ('25', 'ABC/D4T/LPV-r (or ABC/3TC/ALU)'), ('14', 'TRU/RAL'),
        ('15', 'Tenolam/NVP'), ('16', 'Tenolam/LPV/rit'), ('17', 'Tenolam/EFV'),
        ('22', 'AZT/3TC/DTG (or CBV/DTG)(or CBV/Dolutegravir)'),
        ('23', 'CBV/ATZ/rit (or ZDV/3TC/Atazanavir/ritonavir)'),
        ('24', 'TRU/ATZ/rit (or TDF/FTC/Atazanavir/ritonavir)'),
        ('31', 'ABC/3TC/ATZ-r (or ABC/3TC/Atazanavir-ritonavir)'),
        ('27', 'CBV/DRV/rit (or ZDV/3TC/Darunavir/ritonavir)'),
        ('28', 'TRU/DRV/rit (or TDF/FTC/Darunavir/ritonavir)'),
        ('18', 'HAART unspecified'), ('19', 'OTHER')),
        help_text="ALU=Aluvia TRU=Truvada NVP=Nevirapine CBV=Combivir EFV=Efavirenz ABC=Abacavir RAL=Raltegravir DTG=Dolutegravir TAF=Tenofovir Alafenamide ATZ=Atazanavir", )

    otherinitialreg = models.CharField(
        verbose_name="Specify the regimen:",
        max_length=100,
        help_text="", )

    initialreg_source = models.CharField(
        verbose_name="For initial regimen in pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    initialregdate = models.DateField(
        verbose_name="Start date of Initial Regimen:",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    initregdate_est = models.CharField(
        verbose_name="Is any part of this date estimated?",
        max_length=1,
        choices=(('0', 'NONE'), ('1', 'DAY'), ('2', 'MONTH'), ('3', 'YEAR')),
        help_text="", )

    initialregdateunknown = models.CharField(
        verbose_name="Is the start date of Initial regimen UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    initialregdate_source = models.CharField(
        verbose_name="For initial regimen date: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    delivreg = models.CharField(
        verbose_name="Regimen being taken AT DELIVERY",
        max_length=2,
        choices=(
        ('1', 'AZT only'), ('2', 'Atripla (or TDF/FTC/EFV or TRU/EFV or Atroiza)'),
        ('21', 'TDF/FTC/DTG (or TRU/DTG)(or TRU/Dolutegravir)'),
        ('30', 'TDF/3TC/DTG (or TLD or DLT or TDF/3TC/Dolutegravir)'), ('32',
                                                                        'TAF-ED (or TAF/FTC/DTG or Tenofovir Alafenamide/emtricitabine/dolutegravir)'),
        ('29', 'EFV/D4T/3TC'), ('3', 'NVP/CBV (or NVP/AZT/3TC)'),
        ('4', 'ALU/CBV (or ALU/AZT/3TC or LPV/rit/AZT/3TC)'), ('5', 'NVP/D4T/3TC'),
        ('6', 'ALU/D4T/3TC (or LPV/rit/D4T/3TC)'), ('7', 'NVP/TRU (or NVP/TDF/FTC)'),
        ('8', 'ALU/TRU (or ALU/TDF/FTC or LPV/rit/TDF/FTC)'),
        ('9', 'EFV/CBV (or EFV/AZT/3TC)'), ('10', 'EFV/TRU'),
        ('26', 'ABC/3TC/DTG (Abacavir/3TC/Dolutegravir)'), ('11', 'ABC/3TC/NVP'),
        ('12', 'ABC/3TC/LPV/rit'), ('13', 'ABC/3TC/EFV'),
        ('25', 'ABC/D4T/LPV-r (or ABC/3TC/ALU)'), ('14', 'TRU/RAL'),
        ('15', 'Tenolam/NVP'), ('16', 'Tenolam/LPV/rit'), ('17', 'Tenolam/EFV'),
        ('22', 'AZT/3TC/DTG (or CBV/DTG)(or CBV/Dolutegravir)'),
        ('23', 'CBV/ATZ/rit (or ZDV/3TC/Atazanavir/ritonavir)'),
        ('24', 'TRU/ATZ/rit (or TDF/FTC/Atazanavir/ritonavir)'),
        ('31', 'ABC/3TC/ATZ/rit (or ABC/3TC/Atazanavir/ritonavir)'),
        ('27', 'CBV/DRV/rit (or ZDV/3TC/Darunavir/ritonavir)'),
        ('28', 'TRU/DRV/rit (or TDF/FTC/Darunavir/ritonavir)'),
        ('18', 'HAART unspecified'), ('19', 'OTHER'), ('20', 'NONE')),
        help_text="ALU=Aluvia TRU=Truvada NVP=Nevirapine CBV=Combivir EFV=Efavirenz ABC=Abacavir RAL=Raltegravir DTG=Dolutegravir TAF=Tenofovir Alafenamide ATZ=Atazanavir", )

    otherdelivreg = models.CharField(
        verbose_name="Specify the regimen:",
        max_length=100,
        help_text="", )

    delivreg_source = models.CharField(
        verbose_name="For regimen being taken at delivery: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    changearvs = models.CharField(
        verbose_name="Is there documentation of change of ARVs to a new regimen during pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    changearvs_source = models.CharField(
        verbose_name="For change ARVs during pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    changearvs_number = models.CharField(
        verbose_name="How many times were ARVs changed during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    changearvs_number_source = models.CharField(
        verbose_name="For how many times were ARVs changed during pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="", )

    changearvs1_date = models.DateField(
        verbose_name="Date of first change of ARV regimen?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    changearvs1_dateunknonwn = models.CharField(
        verbose_name="Date of first ARV change is UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    changearvs1_date_source = models.CharField(
        verbose_name="For date of first ARV change during pregnancy: Source of information used in the HIV abstraction form? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    changearvs1_reason = models.TextField(
        verbose_name="Reason for first change of ARV regimen?",
        help_text="", )

    changearvs1_reason_source = models.CharField(
        verbose_name="For reason for first ARV change during pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    changearvs1_reg = models.CharField(
        verbose_name="Second ARV regimen in pregnancy?",
        max_length=2,
        choices=(
        ('1', 'AZT only'), ('2', 'Atripla (or TDF/FTC/EFV or TRU/EFV or Atroiza)'),
        ('21', 'TDF/FTC/DTG (or TRU/DTG)(or TRU/Dolutegravir)'),
        ('30', 'TDF/3TC/DTG (or TLD or DLT or TDF/3TC/Dolutegravir)'), ('32',
                                                                        'TAF-ED (or TAF/FTC/DTG or Tenofovir Alafenamide/emtricitabine/dolutegravir)'),
        ('29', 'EFV/D4T/3TC'), ('3', 'NVP/CBV (or NVP/AZT/3TC)'),
        ('4', 'ALU/CBV (or ALU/AZT/3TC or LPV/rit/AZT/3TC)'), ('5', 'NVP/D4T/3TC'),
        ('6', 'ALU/D4T/3TC (or LPV/rit/D4T/3TC)'), ('7', 'NVP/TRU (or NVP/TDF/FTC)'),
        ('8', 'ALU/TRU (or ALU/TDF/FTC or LPV/rit/TDF/FTC)'),
        ('9', 'EFV/CBV (or EFV/AZT/3TC)'), ('10', 'EFV/TRU'),
        ('26', 'ABC/3TC/DTG (Abacavir/3TC/Dolutegravir)'), ('11', 'ABC/3TC/NVP'),
        ('12', 'ABC/3TC/LPV/rit'), ('13', 'ABC/3TC/EFV'),
        ('25', 'ABC/D4T/LPV-r (or ABC/3TC/ALU)'), ('14', 'TRU/RAL'),
        ('15', 'Tenolam/NVP'), ('16', 'Tenolam/LPV/rit'), ('17', 'Tenolam/EFV'),
        ('22', 'AZT/3TC/DTG (or CBV/DTG)(or CBV/Dolutegravir)'),
        ('23', 'CBV/ATZ/rit (or ZDV/3TC/Atazanavir/ritonavir)'),
        ('24', 'TRU/ATZ/rit (or TDF/FTC/Atazanavir/ritonavir)'),
        ('31', 'ABC/3TC/ATZ-r (or ABC/3TC/Atazanavir-ritonavir)'),
        ('27', 'CBV/DRV/rit (or ZDV/3TC/Darunavir/ritonavir)'),
        ('28', 'TRU/DRV/rit (or TDF/FTC/Darunavir/ritonavir)'),
        ('18', 'HAART unspecified'), ('19', 'OTHER')),
        help_text="ALU=Aluvia TRU=Truvada NVP=Nevirapine CBV=Combivir EFV=Efavirenz ABC=Abacavir RAL=Raltegravir", )

    otherchange1_reg = models.CharField(
        verbose_name="Specify the second regimen:",
        max_length=100,
        help_text="", )

    changearvs1_reg_source = models.CharField(
        verbose_name="Second ART regimen during pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    changearvs2_date = models.DateField(
        verbose_name="Date of second change of ARV regimen?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    changearvs2_dateunknown = models.CharField(
        verbose_name="Date of second ARV change is UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    changearvs2_date_source = models.CharField(
        verbose_name="Date of change of second ART regimen during pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    changearvs2_reason = models.TextField(
        verbose_name="Reason for second change of ARV regimen?",
        help_text="", )

    changearvs2_reason_source = models.CharField(
        verbose_name="Reason for switch of second ART regimen during pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    changearvs2_reg = models.CharField(
        verbose_name="Third ARV regimen in pregnancy?",
        max_length=2,
        choices=(
        ('1', 'AZT only'), ('2', 'Atripla (or TDF/FTC/EFV or TRU/EFV or Atroiza)'),
        ('21', 'TDF/FTC/DTG (or TRU/DTG)(or TRU/Dolutegravir)'),
        ('30', 'TDF/3TC/DTG (or TLD or DLT or TDF/3TC/Dolutegravir)'), ('32',
                                                                        'TAF-ED (or TAF/FTC/DTG or Tenofovir Alafenamide/emtricitabine/dolutegravir)'),
        ('29', 'EFV/D4T/3TC'), ('3', 'NVP/CBV (or NVP/AZT/3TC)'),
        ('4', 'ALU/CBV (or ALU/AZT/3TC or LPV/rit/AZT/3TC)'), ('5', 'NVP/D4T/3TC'),
        ('6', 'ALU/D4T/3TC (or LPV/rit/D4T/3TC)'), ('7', 'NVP/TRU (or NVP/TDF/FTC)'),
        ('8', 'ALU/TRU (or ALU/TDF/FTC or LPV/rit/TDF/FTC)'),
        ('9', 'EFV/CBV (or EFV/AZT/3TC)'), ('10', 'EFV/TRU'),
        ('26', 'ABC/3TC/DTG (Abacavir/3TC/Dolutegravir)'), ('11', 'ABC/3TC/NVP'),
        ('12', 'ABC/3TC/LPV/rit'), ('13', 'ABC/3TC/EFV'),
        ('25', 'ABC/D4T/LPV-r (or ABC/3TC/ALU)'), ('14', 'TRU/RAL'),
        ('15', 'Tenolam/NVP'), ('16', 'Tenolam/LPV/rit'), ('17', 'Tenolam/EFV'),
        ('22', 'AZT/3TC/DTG (or CBV/DTG)(or CBV/Dolutegravir)'),
        ('23', 'CBV/ATZ/rit (or ZDV/3TC/Atazanavir/ritonavir)'),
        ('24', 'TRU/ATZ/rit (or TDF/FTC/Atazanavir/ritonavir)'),
        ('27', 'CBV/DRV/rit (or ZDV/3TC/Darunavir/ritonavir)'),
        ('28', 'TRU/DRV/rit (or TDF/FTC/Darunavir/ritonavir)'),
        ('18', 'HAART unspecified'), ('19', 'OTHER')),
        help_text="ALU=Aluvia TRU=Truvada NVP=Nevirapine CBV=Combivir EFV=Efavirenz ABC=Abacavir RAL=Raltegravir", )

    otherchange2_reg = models.CharField(
        verbose_name="Specify the third regimen:",
        max_length=100,
        help_text="", )

    changearvs2_reg_source = models.CharField(
        verbose_name="Third ART regimen during pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    terminatearvs = models.CharField(
        verbose_name="Is there documentation of termination or defaulting of ARVs during pregnancy? (stopping ARVs and not starting onto a new regimen prior to delivery) ",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="If a woman is not on ARVs at time of delivery but was previously on ARVs in pregnancy, termination of ARVs must be \"Yes\"", )

    terminatearvs_source = models.CharField(
        verbose_name="Terminated ART during pregnancy: Source of information used in the HIV abstraction form? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    terminatearvs_date = models.DateField(
        verbose_name="Date of ARV termination/defaulting date?",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    terminatearvs_date_source = models.CharField(
        verbose_name="Date terminated/defaullted ART during pregnancy: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    regimens_prior = models.CharField(
        verbose_name="Was the mother ever on any other ART regimen before pregnancy (different from the initial regimen during this pregnancy)? ",
        max_length=2,
        choices=(('1',
                  'Yes, the mother was on a DIFFERENT ART regimen than the initial regimen in pregnancy (or mother on NO ARVs during pregnancy but was on a regimen before conception)'),
                 ('2',
                  'Yes, the mother was on the SAME ART regimen as the initial regimen in pregnancy but defaulted or terminated or was used just for PMTCT then stopped'),
                 ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    conception_switch_source = models.CharField(
        verbose_name="Was mother on different ART prior to conception: Source of information used? (choose ALL that apply)",
        max_length=1,
        choices=(('1', "Mother's report"), ('2', 'IDCC card'), ('3', 'OB card')),
        help_text="All answers chosen must AGREE (have the same information)", )

    regimens_prior_number = models.CharField(
        verbose_name="How many other regimens was she on PRIOR to conception?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3 or more')),
        help_text="", )

    concept_switch1 = models.CharField(
        verbose_name="Regimen taken MOST RECENTLY prior to current regimen (but prior to pregnancy) ",
        max_length=2,
        choices=(
        ('1', 'AZT only'), ('2', 'Atripla (or TDF/FTC/EFV or TRU/EFV or Atroiza)'),
        ('21', 'TDF/FTC/DTG (or TRU/DTG)(or TRU/Dolutegravir)'),
        ('30', 'TDF/3TC/DTG (or TLD or DLT or TDF/3TC/Dolutegravir)'), ('32',
                                                                        'TAF-ED (or TAF/FTC/DTG or Tenofovir Alafenamide/emtricitabine/dolutegravir)'),
        ('29', 'EFV/D4T/3TC'), ('3', 'NVP/CBV (or NVP/AZT/3TC)'),
        ('4', 'ALU/CBV (or ALU/AZT/3TC or LPV/rit/AZT/3TC)'), ('5', 'NVP/D4T/3TC'),
        ('6', 'ALU/D4T/3TC (or LPV/rit/D4T/3TC)'), ('7', 'NVP/TRU (or NVP/TDF/FTC)'),
        ('8', 'ALU/TRU (or ALU/TDF/FTC or LPV/rit/TDF/FTC)'),
        ('9', 'EFV/CBV (or EFV/AZT/3TC)'), ('10', 'EFV/TRU'),
        ('26', 'ABC/3TC/DTG (Abacavir/3TC/Dolutegravir)'), ('11', 'ABC/3TC/NVP'),
        ('12', 'ABC/3TC/LPV/rit'), ('13', 'ABC/3TC/EFV'),
        ('25', 'ABC/D4T/LPV-r (or ABC/3TC/ALU)'), ('14', 'TRU/RAL'),
        ('15', 'Tenolam/NVP'), ('16', 'Tenolam/LPV/rit'), ('17', 'Tenolam/EFV'),
        ('22', 'AZT/3TC/DTG (or CBV/DTG)(or CBV/Dolutegravir)'),
        ('23', 'CBV/ATZ/rit (or ZDV/3TC/Atazanavir/ritonavir)'),
        ('24', 'TRU/ATZ/rit (or TDF/FTC/Atazanavir/ritonavir)'),
        ('31', 'ABC/3TC/ATZ/rit (or ABC/3TC/Atazanavir/ritonavir)'),
        ('27', 'CBV/DRV/rit (or ZDV/3TC/Darunavir/ritonavir)'),
        ('28', 'TRU/DRV/rit (or TDF/FTC/Darunavir/ritonavir)'),
        ('18', 'HAART unspecified'), ('19', 'OTHER')),
        help_text="ALU=Aluvia TRU=Truvada NVP=Nevirapine CBV=Combivir EFV=Efavirenz ABC=Abacavir RAL=Raltegravir DTG=Dolutegravir TAF=Tenofovir Alafenamide ATZ=Atazanavir", )

    conception_switch1_date = models.DateField(
        verbose_name="Date woman started this regimen (the regimen taken most recently before the current regimen, but before conception)",
        help_text="", )

    conception_switch1_stopdate = models.DateField(
        verbose_name="Date woman terminated or changed this regimen (the regimen taken most recently before the current regimen, but before conception)",
        help_text="", )

    conception_switch1_reason = models.TextField(
        verbose_name="Reason woman terminated or switched this regimen  (the most recent regimen before the current regimen, before conception)",
        help_text="", )

    concept_switch2 = models.CharField(
        verbose_name="Regimen prescribed SECOND most recently before the current regimen (but prior to pregnancy)",
        max_length=2,
        choices=(
        ('1', 'AZT only'), ('2', 'Atripla (or TDF/FTC/EFV or TRU/EFV or Atroiza)'),
        ('21', 'TDF/FTC/DTG (or TRU/DTG)(or TRU/Dolutegravir)'),
        ('30', 'TDF/3TC/DTG (or TLD or DLT or TDF/3TC/Dolutegravir)'), ('32',
                                                                        'TAF-ED (or TAF/FTC/DTG or Tenofovir Alafenamide/emtricitabine/dolutegravir)'),
        ('29', 'EFV/D4T/3TC'), ('3', 'NVP/CBV (or NVP/AZT/3TC)'),
        ('4', 'ALU/CBV (or ALU/AZT/3TC or LPV/rit/AZT/3TC)'), ('5', 'NVP/D4T/3TC'),
        ('6', 'ALU/D4T/3TC (or LPV/rit/D4T/3TC)'), ('7', 'NVP/TRU (or NVP/TDF/FTC)'),
        ('8', 'ALU/TRU (or ALU/TDF/FTC or LPV/rit/TDF/FTC)'),
        ('9', 'EFV/CBV (or EFV/AZT/3TC)'), ('10', 'EFV/TRU'),
        ('26', 'ABC/3TC/DTG (Abacavir/3TC/Dolutegravir)'), ('11', 'ABC/3TC/NVP'),
        ('12', 'ABC/3TC/LPV/rit'), ('13', 'ABC/3TC/EFV'),
        ('25', 'ABC/D4T/LPV-r (or ABC/3TC/ALU)'), ('14', 'TRU/RAL'),
        ('15', 'Tenolam/NVP'), ('16', 'Tenolam/LPV/rit'), ('17', 'Tenolam/EFV'),
        ('22', 'AZT/3TC/DTG (or CBV/DTG)(or CBV/Dolutegravir)'),
        ('23', 'CBV/ATZ/rit (or ZDV/3TC/Atazanavir/ritonavir)'),
        ('24', 'TRU/ATZ/rit (or TDF/FTC/Atazanavir/ritonavir)'),
        ('31', 'ABC/3TC/ATZ-r (or ABC/3TC/Atazanavir-ritonavir)'),
        ('27', 'CBV/DRV/rit (or ZDV/3TC/Darunavir/ritonavir)'),
        ('28', 'TRU/DRV/rit (or TDF/FTC/Darunavir/ritonavir)'),
        ('18', 'HAART unspecified'), ('19', 'OTHER')),
        help_text="ALU=Aluvia TRU=Truvada NVP=Nevirapine CBV=Combivir EFV=Efavirenz ABC=Abacavir RAL=Raltegravir DTG=Dolutegravir TAF=Tenofovir Alafenamide ATZ=Atazanavir", )

    conception_switch2_date = models.DateField(
        verbose_name="Date woman switched to her SECOND most recent regimen (before conception)",
        help_text="", )

    conception_switch2_stopdate = models.DateField(
        verbose_name="Date woman terminated or stopped the SECOND most recent regimen?",
        help_text="", )

    conception_switch2_reason = models.TextField(
        verbose_name="Reason woman switched to her SECOND most recent regimen (before conception)",
        help_text="", )

    concept_switch3 = models.CharField(
        verbose_name="Regimen prescribed THIRD most recently before the current regimen (but prior to pregnancy)",
        max_length=2,
        choices=(
        ('1', 'AZT only'), ('2', 'Atripla (or TDF/FTC/EFV or TRU/EFV or Atroiza)'),
        ('21', 'TDF/FTC/DTG (or TRU/DTG)(or TRU/Dolutegravir)'),
        ('30', 'TDF/3TC/DTG (or TLD or DLT or TDF/3TC/Dolutegravir)'), ('32',
                                                                        'TAF-ED (or TAF/FTC/DTG or Tenofovir Alafenamide/emtricitabine/dolutegravir)'),
        ('29', 'EFV/D4T/3TC'), ('3', 'NVP/CBV (or NVP/AZT/3TC)'),
        ('4', 'ALU/CBV (or ALU/AZT/3TC or LPV/rit/AZT/3TC)'), ('5', 'NVP/D4T/3TC'),
        ('6', 'ALU/D4T/3TC (or LPV/rit/D4T/3TC)'), ('7', 'NVP/TRU (or NVP/TDF/FTC)'),
        ('8', 'ALU/TRU (or ALU/TDF/FTC or LPV/rit/TDF/FTC)'),
        ('9', 'EFV/CBV (or EFV/AZT/3TC)'), ('10', 'EFV/TRU'),
        ('26', 'ABC/3TC/DTG (Abacavir/3TC/Dolutegravir)'), ('11', 'ABC/3TC/NVP'),
        ('12', 'ABC/3TC/LPV/rit'), ('13', 'ABC/3TC/EFV'),
        ('25', 'ABC/D4T/LPV-r (or ABC/3TC/ALU)'), ('14', 'TRU/RAL'),
        ('15', 'Tenolam/NVP'), ('16', 'Tenolam/LPV/rit'), ('17', 'Tenolam/EFV'),
        ('22', 'AZT/3TC/DTG (or CBV/DTG)(or CBV/Dolutegravir)'),
        ('23', 'CBV/ATZ/rit (or ZDV/3TC/Atazanavir/ritonavir)'),
        ('24', 'TRU/ATZ/rit (or TDF/FTC/Atazanavir/ritonavir)'),
        ('31', 'ABC/3TC/ATZ-r (or ABC/3TC/Atazanavir-ritonavir)'),
        ('27', 'CBV/DRV/rit (or ZDV/3TC/Darunavir/ritonavir)'),
        ('28', 'TRU/DRV/rit (or TDF/FTC/Darunavir/ritonavir)'),
        ('18', 'HAART unspecified'), ('19', 'OTHER')),
        help_text="ALU=Aluvia TRU=Truvada NVP=Nevirapine CBV=Combivir EFV=Efavirenz ABC=Abacavir RAL=Raltegravir DTG=Dolutegravir TAF=Tenofovir Alafenamide ATZ=Atazanavir", )

    conception_switch3_date = models.DateField(
        verbose_name="Date woman switched to her THIRD most recent regimen (before conception)",
        help_text="", )

    conception_switch3_stopdate = models.DateField(
        verbose_name="Date woman terminated or stopped the SECOND most recent regimen?",
        help_text="", )

    conception_switch3_reason = models.TextField(
        verbose_name="Reason woman switched to her THIRD most recent regimen (before conception)",
        help_text="", )

    arvcomments = models.TextField(
        verbose_name="Comments about ARVs (please note clarifications, questions, or a disruption of ARVs >1 week)",
        blank=True, null=True,
        help_text="", )

    lmp = models.DateField(
        verbose_name="Last Menstrual Period (LMP):",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    lmpunknown = models.CharField(
        verbose_name="Is the LMP unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    plot_changed = models.CharField(
        verbose_name="Is there documentation that the original growth plot has been changed (ie pregnancy was 're-plotted' or 're-dated' or  'EDD was changed')?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    replot_reason = models.CharField(
        verbose_name="The reason documented for re-plotting is:",
        max_length=2,
        choices=(
        ('1', 'Based on ultrasound'), ('2', 'Based on measurements (eg, fundal height)'),
        ('4', 'miscalculation'), ('3', 'Other'), ('99', 'Unknown')),
        help_text="", )

    replot_reason_other = models.TextField(
        verbose_name="Reason for re-plotting, other:",
        help_text="", )

    ultrasound = models.CharField(
        verbose_name="Is there documentation that this woman had a an ultrasound scan?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    ultrasound_date = models.DateField(
        verbose_name="Date of FIRST prenatal ultrasound",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    ultrasound_date_unk = models.CharField(
        verbose_name="Date of first prenatal ultrasound is unknown",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    ancvisits = models.PositiveIntegerField(
        verbose_name="How many clinic visits during the current pregnancy? (include even if only weight or blood pressure was checked)",
        blank=True, null=True,
        help_text="If UNKNOWN because all pages are missing, Leave BLANK. If non-booker, write 0", )

    ancvisitsunknown = models.CharField(
        verbose_name="Are the number of clinic visits UNKNOWN",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    scheduledanc = models.CharField(
        verbose_name="How many of these clinic visits were scheduled ANC clinic visits (the mother was seen by a midwife)? (exclude sick visits, visits just for blood pressure or weight check, etc).",
        max_length=2,
        choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                 ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
                 ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
                 ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')),
        help_text="", )

    refbeforedel = models.CharField(
        verbose_name="Referred to this site FOR DELIVERY because of complication in pregnancy, labor or delivery?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    reason_rbd = models.CharField(
        verbose_name="Reason for Referral before Delivery",
        max_length=2,
        choices=(('1', 'Primigravid and age >30'), ('28', 'Primigravid (age not >30)'),
                 ('2', 'Age < 18'), ('3', 'Age >35'), ('4',
                                                       'Hypertension, Pre-ecclampsia or Ecclampsia (High BP, high blood pressure, elevated BP, PIH, Pregnancy Induced Hypertension, gestational hypertension)'),
                 ('5', 'Scheduled C-section'), ('15', 'Prior C-section'), ('6',
                                                                           'Other medical problem with the mother (such as heart problem, kidney problem, etc)'),
                 ('7', 'Infection'), ('8',
                                      'Problem with the baby noted during antenatal care (but NOT a congenital abnormality)'),
                 ('9', 'Congenital abnormality of infant noted during antenatal care'),
                 ('10', 'Concern for the baby (fetal distress)'),
                 ('11', 'PPROM (Preterm Premature rupture of membranes)'),
                 ('23', 'PROM/SROM'), ('12', 'Premature Labor'), ('16', 'anemia'),
                 ('17', 'Antepartum hemorrhage (APH)/PV bleeding'),
                 ('18', 'Bad Obstetric History (BOH)'), ('19', 'IUFD (fetal demise)'),
                 ('20', 'CPD/Big baby (cephalo-pelvic disproportion)'),
                 ('21', 'post-dates'),
                 ('22', 'presentation of the baby (e.g breech, footling, transverse)'),
                 ('25', 'failed induction'), ('26', 'multiparous/grand multip'),
                 ('24', 'Failure to progress/stalled labor/prolonged labor'),
                 ('27', 'Placenta previa'), ('29', 'twin (or triplet) pregnancy'),
                 ('30', 'for Labor Pains/ for Delivery'), ('13', 'UNKNOWN'),
                 ('14', 'OTHER')),
        help_text="Choose All that Apply", )

    otherreason_rbd = models.TextField(
        verbose_name="If other reason for referral, specify:",
        help_text="", )

    height = models.CharField(
        verbose_name="Does patient have HEIGHT recorded?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    height_cm = models.CharField(
        verbose_name="Height (in METERS)",
        max_length=100,
        help_text="100 CM = 1 METER (so 140 CM =1.4 Meters). Must use 1 decimal point.", )

    prepreg_wt = models.CharField(
        verbose_name="Pre-Pregnancy Weight (in kilograms)",
        max_length=100,
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank. Must use 1 decimal point (eg. 56.0)", )

    prepregwt_unknown = models.CharField(
        verbose_name="Is Pre-Pregnancy Weight UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    prepregwt_date = models.DateField(
        verbose_name="Date of Pre-Pregnancy Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    prepreg_wtdateunknown = models.CharField(
        verbose_name="Is the date of pre-pregnancy weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    number_wts = models.CharField(
        verbose_name="How many weights are recorded in pregnancy?",
        max_length=2,
        choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                 ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
                 ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
                 ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'),
                 ('21', 'more than 20')),
        help_text="", )

    firstwt = models.CharField(
        verbose_name="First Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal place (eg 56.0) ", )

    firstwtdat = models.DateField(
        verbose_name="Date of First Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    firstwt_dateunknown = models.CharField(
        verbose_name="Is the date of first weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        blank=True, null=True,
        help_text="", )

    wt2 = models.CharField(
        verbose_name="Second Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate2 = models.DateField(
        verbose_name="Date of second Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt2_dateunknown = models.CharField(
        verbose_name="Is the date of second weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt3 = models.CharField(
        verbose_name="Third Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate3 = models.DateField(
        verbose_name="Date of 3rd Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt3_dateunknown = models.CharField(
        verbose_name="Is the date of third weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt4 = models.CharField(
        verbose_name="Fourth Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate4 = models.DateField(
        verbose_name="Date of 4th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt4_dateunknown = models.CharField(
        verbose_name="Is the date of fourth weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt5 = models.CharField(
        verbose_name="Fifth Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate5 = models.DateField(
        verbose_name="Date of 5th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt5_dateunknown = models.CharField(
        verbose_name="Is the date of 5th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt6 = models.CharField(
        verbose_name="6th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate6 = models.DateField(
        verbose_name="Date of 6th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt6_dateunknown = models.CharField(
        verbose_name="Is the date of 6th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt7 = models.CharField(
        verbose_name="7th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate7 = models.DateField(
        verbose_name="Date of 7th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt7_dateunknown = models.CharField(
        verbose_name="Is the date of 7th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt8 = models.CharField(
        verbose_name="8th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate8 = models.DateField(
        verbose_name="Date of 8th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt8_dateunknown = models.CharField(
        verbose_name="Is the date of 8th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt9 = models.CharField(
        verbose_name="9th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate9 = models.DateField(
        verbose_name="Date of 9th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt9_dateunknown = models.CharField(
        verbose_name="Is the date of 9th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt10 = models.CharField(
        verbose_name="10th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate10 = models.DateField(
        verbose_name="Date of 10th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt10_dateunknown = models.CharField(
        verbose_name="Is the date of 10th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt11 = models.CharField(
        verbose_name="11th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate11 = models.DateField(
        verbose_name="Date of 11th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt11_dateunknown = models.CharField(
        verbose_name="Is the date of 11th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt12 = models.CharField(
        verbose_name="12th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate12 = models.DateField(
        verbose_name="Date of 12th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt12_dateunknown = models.CharField(
        verbose_name="Is the date of 12th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt13 = models.CharField(
        verbose_name="13th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate13 = models.DateField(
        verbose_name="Date of 13th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt13_dateunknown = models.CharField(
        verbose_name="Is the date of 13th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt14 = models.CharField(
        verbose_name="14th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate14 = models.DateField(
        verbose_name="Date of 14th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt14_dateunknown = models.CharField(
        verbose_name="Is the date of 14th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt15 = models.CharField(
        verbose_name="15th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate15 = models.DateField(
        verbose_name="Date of 15th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt15_dateunknown = models.CharField(
        verbose_name="Is the date of 15th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt16 = models.CharField(
        verbose_name="16th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate16 = models.DateField(
        verbose_name="Date of 16th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt16_dateunknown = models.CharField(
        verbose_name="Is the date of 16th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt17 = models.CharField(
        verbose_name="17th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate17 = models.DateField(
        verbose_name="Date of 17th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt17_dateunknown = models.CharField(
        verbose_name="Is the date of 17th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt18 = models.CharField(
        verbose_name="18th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate18 = models.DateField(
        verbose_name="Date of 18th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt18_dateunknown = models.CharField(
        verbose_name="Is the date of 18th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt19 = models.CharField(
        verbose_name="19th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate19 = models.DateField(
        verbose_name="Date of 19th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt19_dateunknown = models.CharField(
        verbose_name="Is the date of 19th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    wt20 = models.CharField(
        verbose_name="20th Weight Recorded in Pregnancy(kg)",
        max_length=100,
        help_text="Must use 1 decimal point (eg. 56.0)", )

    wtdate20 = models.DateField(
        verbose_name="Date of 20th Weight:",
        blank=True, null=True,
        help_text="MM - DD - YY ", )

    wt20_dateunknown = models.CharField(
        verbose_name="Is the date of 20th weight unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    bloodpress = models.CharField(
        verbose_name="Does this patient have any Blood Pressures Recorded in Pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    systolic130 = models.CharField(
        verbose_name="Are any recorded SYSTOLIC (the top number) Blood pressure >=140?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="If BP is written 130/40, 130 is the SYSTOLIC BP", )

    diastolic_bp = models.CharField(
        verbose_name="Are any DIASTOLIC (the bottom number) Blood Pressure >=90",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="If BP is written 130/40, 40 is the DIASTOLIC", )

    lastbp_date = models.DateField(
        verbose_name="Date of Last BP recorded prior to admission for labor and delivery? (this is the last BP recorded in clinic notes BEFORE coming to the hospital for delivery)",
        help_text="", )

    nohtn_bpmed = models.CharField(
        verbose_name="Was this woman ever started on high BP medication?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    nohtn_bpmedspecify = models.CharField(
        verbose_name="Which Blood Pressure medications were started DURING PREGNANCY?",
        max_length=2,
        choices=(('1', 'Methyldopa'), ('2', 'Nifedipine'), ('3', 'Hydralazine'),
                 ('4', 'Hydrochlorothiazide (HCTZ)'), ('5', 'Enalapril'),
                 ('6', 'Captopril'), ('7', 'Atenolol'), ('8', 'Other'), ('0', 'NONE'),
                 ('99', 'UNKNOWN')),
        help_text="Check All that Apply", )

    nohtn_bpmedother = models.TextField(
        verbose_name="What 'Other' BP medication was started",
        help_text="", )

    lastsystolicbp = models.PositiveIntegerField(
        verbose_name="Last Systolic BP recorded in pregnancy?(this is the last systolic BP recorded in clinic notes prior to admission to the hospital for delivery)",
        help_text="", )

    lastdiastolic_bp = models.PositiveIntegerField(
        verbose_name="Last Diastolic BP recorded in pregnancy?(this is the last systolic BP recorded in clinic notes prior to admission to the hospital for delivery)",
        help_text="", )

    number_bp = models.CharField(
        verbose_name="How many Blood Pressures are recorded in Pregnancy after (and including) the first HIGH BP?",
        max_length=2,
        choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                 ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
                 ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
                 ('16', 'more than 15')),
        help_text="", )

    bp1_date = models.DateField(
        verbose_name="Date of First HIGH BP? (systolic >=140 or diastolic >=90)",
        help_text="", )

    systolic1 = models.PositiveIntegerField(
        verbose_name="Systolic BP recorded on date of first HIGH BP in pregnancy?(either this systolic should be >=140 OR diastolic from this date should be >=90 or both)",
        help_text="", )

    diastolic1 = models.PositiveIntegerField(
        verbose_name="Diastolic BP recorded on the date of first HIGH BP in pregnancy?(either this systolic should be >=90 OR systolic from this date should be >=140 or both)",
        help_text="", )

    bp2_date = models.DateField(
        verbose_name="Date of 2nd BP?(This is the BP recorded after the first HIGH BP)",
        help_text="MM - DD - YY ", )

    systolic2 = models.PositiveIntegerField(
        verbose_name="2nd Systolic BP recorded in pregnancy?(This is the systolic BP recorded after the first HIGH BP-no matter if the 2nd is high or normal)",
        help_text="", )

    diastolic2 = models.PositiveIntegerField(
        verbose_name="2nd diastolic BP recorded in pregnancy?",
        help_text="", )

    bp3_date = models.DateField(
        verbose_name="Date of 3rd BP?",
        help_text="MM - DD - YY ", )

    systolic3 = models.PositiveIntegerField(
        verbose_name="3rd Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic3 = models.PositiveIntegerField(
        verbose_name="3rd diastolic BP recorded in pregnancy?",
        help_text="", )

    bp4_date = models.DateField(
        verbose_name="Date of 4th BP?",
        help_text="MM - DD - YY ", )

    systolic4 = models.PositiveIntegerField(
        verbose_name="4th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic4 = models.PositiveIntegerField(
        verbose_name="4th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp5_date = models.DateField(
        verbose_name="Date of 5th BP?",
        help_text="MM - DD - YY ", )

    systolic5 = models.PositiveIntegerField(
        verbose_name="5th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic5 = models.PositiveIntegerField(
        verbose_name="5th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp6_date = models.DateField(
        verbose_name="Date of 6th BP?",
        help_text="MM - DD - YY ", )

    systolic6 = models.PositiveIntegerField(
        verbose_name="6th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic6 = models.PositiveIntegerField(
        verbose_name="6th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp7_date = models.DateField(
        verbose_name="Date of 7th BP?",
        help_text="MM - DD - YY ", )

    systolic7 = models.PositiveIntegerField(
        verbose_name="7th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic7 = models.PositiveIntegerField(
        verbose_name="7th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp8_date = models.DateField(
        verbose_name="Date of 8th BP?",
        help_text="MM - DD - YY ", )

    systolic8 = models.PositiveIntegerField(
        verbose_name="8th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic8 = models.PositiveIntegerField(
        verbose_name="8th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp9_date = models.DateField(
        verbose_name="Date of 9th BP?",
        help_text="MM - DD - YY ", )

    systolic9 = models.PositiveIntegerField(
        verbose_name="9th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic9 = models.PositiveIntegerField(
        verbose_name="9th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp10_date = models.DateField(
        verbose_name="Date of 10th BP?",
        help_text="MM - DD - YY ", )

    systolic10 = models.PositiveIntegerField(
        verbose_name="10th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic10 = models.PositiveIntegerField(
        verbose_name="10th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp11_date = models.DateField(
        verbose_name="Date of 11th BP?",
        help_text="MM - DD - YY ", )

    systolic11 = models.PositiveIntegerField(
        verbose_name="11th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic11 = models.PositiveIntegerField(
        verbose_name="11th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp12_date = models.DateField(
        verbose_name="Date of 12th BP?",
        help_text="MM - DD - YY ", )

    systolic12 = models.PositiveIntegerField(
        verbose_name="12th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic12 = models.PositiveIntegerField(
        verbose_name="12th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp13_date = models.DateField(
        verbose_name="Date of 13th BP?",
        help_text="MM - DD - YY ", )

    systolic13 = models.PositiveIntegerField(
        verbose_name="13th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic13 = models.PositiveIntegerField(
        verbose_name="13th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp14_date = models.DateField(
        verbose_name="Date of 14th BP?",
        help_text="MM - DD - YY ", )

    systolic14 = models.PositiveIntegerField(
        verbose_name="14th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic14 = models.PositiveIntegerField(
        verbose_name="14th diastolic BP recorded in pregnancy?",
        help_text="", )

    bp15_date = models.DateField(
        verbose_name="Date of 15th BP?",
        help_text="MM - DD - YY ", )

    systolic15 = models.PositiveIntegerField(
        verbose_name="15th Systolic BP recorded in pregnancy?",
        help_text="", )

    diastolic15 = models.PositiveIntegerField(
        verbose_name="15th diastolic BP recorded in pregnancy?",
        help_text="", )

    urineprotein_7aug2015 = models.CharField(
        verbose_name="Did this woman ever have a urine protein?",
        max_length=1,
        choices=(('1', 'No urine protein reported'), ('2', 'Yes, 3+ protein'),
                 ('3', 'Yes, 2+ protein'), ('4', 'Yes, 1+ protein'), ('5', 'Yes, trace')),
        help_text="", )

    ecclampsia = models.CharField(
        verbose_name="Was this woman ever diagnosed with Pre-Ecclampsia or Ecclampsia?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'No')),
        help_text="", )

    urineprotein = models.CharField(
        verbose_name="Is there documentation of positive urine protein?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    bp_med = models.CharField(
        verbose_name="Was any blood pressure medication started during pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="BP meds include: methyldopa, atenolol, carvedilol, nifedipine", )

    bp_med1 = models.CharField(
        verbose_name="Which Blood Pressure medications were started or continued DURING PREGNANCY?",
        max_length=2,
        choices=(('1', 'Methyldopa'), ('2', 'Nifedipine'), ('3',
                                                            'Hydralazine (only if given as a long-term medication, if only given as a one-time dose, do not tick)'),
                 ('4', 'Hydrochlorothiazide (HCTZ)'), ('5', 'Enalapril'),
                 ('6', 'Captopril'), ('7', 'Atenolol'), ('8', 'Other'), ('0', 'NONE'),
                 ('99', 'UNKNOWN')),
        help_text="Check All that Apply", )

    other_bpmed = models.TextField(
        verbose_name="Specify OTHER BP Med",
        help_text="", )

    date_methydopa = models.DateField(
        verbose_name="DATE Methyldopa was started?",
        blank=True, null=True,
        help_text="", )

    methydopa_dateunknown = models.CharField(
        verbose_name="Is the DATE Methyldopa was started UNKNOWN",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    date_nifedipine = models.DateField(
        verbose_name="DATE Nifedipine was started?",
        blank=True, null=True,
        help_text="", )

    nifedipine_dateunknown = models.CharField(
        verbose_name="Is the DATE Nifedpipine was started UNKNOWN",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    date_hydralazine = models.DateField(
        verbose_name="DATE Hydralazine was started?",
        blank=True, null=True,
        help_text="", )

    hydralazine_dateunknown = models.CharField(
        verbose_name="Is the DATE Hydralazine was started UNKNOWN",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    date_hctz = models.DateField(
        verbose_name="DATE Hydrocholothiazide (HCTZ) was started?",
        blank=True, null=True,
        help_text="", )

    hctz_dateunknown = models.CharField(
        verbose_name="Is the DATE Hydrocholorothiazide (HCTZ) was started UNKNOWN",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    date_enalapril = models.DateField(
        verbose_name="DATE Enalapril was started?",
        blank=True, null=True,
        help_text="", )

    enalapril_dateunknown = models.CharField(
        verbose_name="Is the DATE Enalapril was started UNKNOWN",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    date_captopril = models.DateField(
        verbose_name="DATE Captopril was started?",
        blank=True, null=True,
        help_text="", )

    captopril_dateunknown = models.CharField(
        verbose_name="Is the DATE Captopril was started UNKNOWN",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    date_atenolol = models.DateField(
        verbose_name="DATE Atenolol was started?",
        blank=True, null=True,
        help_text="", )

    atenolol_dateunknown = models.CharField(
        verbose_name="Is the DATE Atenolol was started UNKNOWN",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    date_otherbp = models.DateField(
        verbose_name="DATE Other BP med was started?",
        blank=True, null=True,
        help_text="", )

    atenolol_dateunknown2_8ed = models.CharField(
        verbose_name="Is the DATE Other BP Med was started UNKNOWN",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    methyldopa_change1 = models.CharField(
        verbose_name="Was the dose or frequency of Methyldopa ever INCREASED from the starting dose?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    methyldopa_timeschanged = models.CharField(
        verbose_name="How many times was the Methyldopa dose or frequency INCREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4 or more')),
        help_text="", )

    nifedipine_increase = models.CharField(
        verbose_name="Was the dose or frequency of Nifedipine ever INCREASED from the starting dose?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    nifedipine_timeschange = models.CharField(
        verbose_name="How many times was the Nifedipine dose or frequency INCREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4 or more')),
        help_text="", )

    hydralazine_increase = models.CharField(
        verbose_name="Was the dose or frequency of Hydralazine ever INCREASED from the starting dose?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    hydralazine_timeschange = models.CharField(
        verbose_name="How many times was the Hydralazine dose or frequency INCREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4 or more')),
        help_text="", )

    hctz_increase = models.CharField(
        verbose_name="Was the dose or frequency of Hydrochlorothiazide (HCTZ) ever INCREASED from the starting dose?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    hctz_timeschange = models.CharField(
        verbose_name="How many times was the Hydrochlorthiazide (HCTZ) dose or frequency INCREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4 or more')),
        help_text="", )

    enalapril_increase = models.CharField(
        verbose_name="Was the dose or frequency of Enalapril ever INCREASED from the starting dose?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    enalapril_timeschange = models.CharField(
        verbose_name="How many times was the Enalapril dose or frequency INCREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4 or more')),
        help_text="", )

    captopril_increase = models.CharField(
        verbose_name="Was the dose or frequency of Captopril ever INCREASED from the starting dose?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    captopril_timeschange = models.CharField(
        verbose_name="How many times was the Captopril dose or frequency INCREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4 or more')),
        help_text="", )

    atenolol_increase = models.CharField(
        verbose_name="Was the dose or frequency of Atenolol ever INCREASED from the starting dose?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    atenolol_timeschange = models.CharField(
        verbose_name="How many times was the Atenolol dose or frequency INCREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4 or more')),
        help_text="", )

    otherbp_increase = models.CharField(
        verbose_name="Was the dose or frequency of Other BP Med ever INCREASED from the starting dose?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    otherbp_timeschange = models.CharField(
        verbose_name="How many times was the Other BP Med dose or frequency INCREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4 or more')),
        help_text="", )

    methyldopa_decrease = models.CharField(
        verbose_name="Was the dose or frequency of Methyldopa ever DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    methyldopa_timesdecreased = models.CharField(
        verbose_name="How many times was the Methyldopa dose or frequency DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    nifedipine_decrease = models.CharField(
        verbose_name="Was the dose or frequency of Nifedipine ever DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    nifedipine_timesdecrese = models.CharField(
        verbose_name="How many times was the Nifedpipine dose or frequency DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    hydralazine_decrease = models.CharField(
        verbose_name="Was the dose or frequency of Hydralazine ever DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    hydralazine_timesdecrese = models.CharField(
        verbose_name="How many times was the Hydralazine dose or frequency DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    hctz_decrease = models.CharField(
        verbose_name="Was the dose or frequency of Hydrochlorothiazide (HCTZ) ever DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    hctz_timesdecrease = models.CharField(
        verbose_name="How many times was the Hydrochlorothiazide (HCTZ) dose or frequency DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    enalapril_decrease = models.CharField(
        verbose_name="Was the dose or frequency of Enalapril ever DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    enalapril_timesdecrease = models.CharField(
        verbose_name="How many times was the Enalapril dose or frequency DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    captopril_decrease = models.CharField(
        verbose_name="Was the dose or frequency of Captopril ever DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    captopril_timesdecrease = models.CharField(
        verbose_name="How many times was the Captopril dose or frequency DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    atenolol_decrease = models.CharField(
        verbose_name="Was the dose or frequency of Atenolol ever DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    atenolol_timesdecrease = models.CharField(
        verbose_name="How many times was the Atenolol dose or frequency DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    otherbp_decrease = models.CharField(
        verbose_name="Was the dose or frequency of Other BP Med ever DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    otherbp_timesdecrease = models.CharField(
        verbose_name="How many times was the Other BP Med dose or frequency DECREASED during pregnancy?",
        max_length=1,
        choices=(('1', '1'), ('2', '2 or more')),
        help_text="", )

    methyldopa_increase1 = models.DateField(
        verbose_name="Date of FIRST Methyldopa increase?",
        blank=True, null=True,
        help_text="", )

    methydopa_increase1unknown = models.CharField(
        verbose_name="Is the DATE of FIRST Methyldopa INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    methyldopa_increase2 = models.DateField(
        verbose_name="Date of SECOND Methyldopa increase?",
        blank=True, null=True,
        help_text="", )

    methydopa_increase2unknown = models.CharField(
        verbose_name="Is the DATE of SECOND Methyldopa INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    methyldopa_increase3 = models.DateField(
        verbose_name="Date of THIRD Methyldopa increase?",
        blank=True, null=True,
        help_text="", )

    methydopa_increase3unknown = models.CharField(
        verbose_name="Is the DATE of THIRD Methyldopa INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    methyldopa_increase4 = models.DateField(
        verbose_name="Date of FOURTH Methyldopa increase?",
        blank=True, null=True,
        help_text="", )

    methydopa_increase4unknown = models.CharField(
        verbose_name="Is the DATE of FOURTH Methyldopa INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    nifedipine_increase1 = models.DateField(
        verbose_name="Date of FIRST Nifedipine increase?",
        blank=True, null=True,
        help_text="", )

    nifedipine_increase1unk = models.CharField(
        verbose_name="Is the DATE of FIRST Nifedipine INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    nifedipine_increase2 = models.DateField(
        verbose_name="Date of SECOND Nifedipine increase?",
        blank=True, null=True,
        help_text="", )

    nifedipine_increase2unk = models.CharField(
        verbose_name="Is the DATE of SECOND Nifedipine INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    nifedipine_increase3 = models.DateField(
        verbose_name="Date of THIRD Nifedipine increase?",
        blank=True, null=True,
        help_text="", )

    nifedipine_increase3unk = models.CharField(
        verbose_name="Is the DATE of Third Nifedipine INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    nifedipine_increase4 = models.DateField(
        verbose_name="Date of FOURTH Nifedipine increase?",
        blank=True, null=True,
        help_text="", )

    nifedipine_increase4unk = models.CharField(
        verbose_name="Is the DATE of FOURTH Nifedipine INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    hydralazine_increase1 = models.DateField(
        verbose_name="Date of FIRST Hydralazine increase?",
        blank=True, null=True,
        help_text="", )

    hydralazine_increase1unk = models.CharField(
        verbose_name="Is the DATE of FIRST Hydralazine INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    hydralazine_increase2 = models.DateField(
        verbose_name="Date of SECOND Hydralazine increase?",
        blank=True, null=True,
        help_text="", )

    hydralazine_increase2unk = models.CharField(
        verbose_name="Is the DATE of SECOND Hydralazine INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    hydralazine_increase3 = models.DateField(
        verbose_name="Date of THIRD Hydralazine increase?",
        blank=True, null=True,
        help_text="", )

    hydralazine_increase3unk = models.CharField(
        verbose_name="Is the DATE of THIRD Hydralazine INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    hydralazine_increase4 = models.DateField(
        verbose_name="Date of FOURTH Hydralazine increase?",
        blank=True, null=True,
        help_text="", )

    hydralazine_increase4unk = models.CharField(
        verbose_name="Is the DATE of FOURTH Hydralazine INCREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    methyldopa_decrease1 = models.DateField(
        verbose_name="Date of FIRST Methyldopa decrease?",
        blank=True, null=True,
        help_text="", )

    methydopa_decrease1unknown = models.CharField(
        verbose_name="Is the DATE of FIRST Methyldopa DECREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    methyldopa_decrease2 = models.DateField(
        verbose_name="Date of SECOND Methyldopa decrease?",
        blank=True, null=True,
        help_text="", )

    methydopa_decrease2unknown = models.CharField(
        verbose_name="Is the DATE of SECOND Methyldopa DECREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    nifedipine_decrease1 = models.DateField(
        verbose_name="Date of FIRST Nifedipine decrease?",
        blank=True, null=True,
        help_text="", )

    nifedipine_decrease1unk = models.CharField(
        verbose_name="Is the DATE of FIRST Nifedipine DECREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    nifedipine_decrease2 = models.DateField(
        verbose_name="Date of SECOND Nifedipine decrease?",
        blank=True, null=True,
        help_text="", )

    nifedipine_decrease2unk = models.CharField(
        verbose_name="Is the DATE of SECOND Nifedipine DECREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    hydralazine_decrease1 = models.DateField(
        verbose_name="Date of FIRST Hydralazine decrease?",
        blank=True, null=True,
        help_text="", )

    hydralazine_decrease2unk = models.CharField(
        verbose_name="Is the DATE of FIRST Hydralazine DECREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    hydralazine_decrease2 = models.DateField(
        verbose_name="Date of SECOND Hydralazine decrease?",
        blank=True, null=True,
        help_text="", )

    hydral_decrease2unk = models.CharField(
        verbose_name="Is the DATE of SECOND Hydralazine DECREASE UNKNOWN?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    bp_comment = models.TextField(
        verbose_name="Comments on Blood Pressure (for example, was the patient given 1 dose of hydralazine to see if her blood pressure would come down?  Or a fourth BP medication was started? etc.)",
        blank=True, null=True,
        help_text="", )

    was_this_woman_aspirin = models.CharField(
        verbose_name="Is there documentation the woman took aspirin 75mg (sometimes written ASA 75mg) during pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    date_aspirin_started = models.DateField(
        verbose_name="What was the start date of aspirin 75mg?",
        blank=True, null=True,
        help_text="if unknown leave blank", )

    date_aspirin_unknown = models.CharField(
        verbose_name="Is the start date of aspirin 75mg unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    aspirin_ongoing = models.CharField(
        verbose_name=" Is the aspirin 75mg ongoing (at the time of admission for delivery)?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    date_aspirin_stopped = models.DateField(
        verbose_name="What was the stop date for aspirin 75mg?",
        blank=True, null=True,
        help_text="if unknown leave blank", )

    date_asp_stopped_unknw = models.CharField(
        verbose_name="Is the stop date for aspirin 75mg unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    anymatdiag = models.CharField(
        verbose_name="Maternal Diagnoses during Pregnancy:",
        max_length=2,
        choices=(('1', 'Herpes (HSV)/Genital Ulcers/Genital Sores'),
                 ('2', 'Varicella (chicken pox or zoster)'), ('3', 'Rubella'),
                 ('4', 'Toxoplasmosis'), ('5', 'Syphilis (VDRL +, VDRL-reactive)'), ('6',
                                                                                     'Cervicitis/STD/Vaginal Discharge Syndrome (VDS) (sometimes listed as PVD, vaginitis or specific STD like gonorrhea (GC), chlamydia (CT), trichomoniasis (TV))'),
                 ('7',
                  'High Blood Pressure (High BP, hypertension, elevated BP, Gestational Hypertension, PIH, Pregnancy Induced Hypertension)'),
                 ('12', 'Pre-Ecclampsia or Ecclampsia'), ('9', 'Diabetes'),
                 ('10', 'UTI/Pyelonephritis'), ('11', 'Anemia'), ('13', 'Malaria'),
                 ('14', 'TB'), ('15', 'abscess'), ('16', 'asthma'), ('17', 'breast lump'),
                 ('18', 'Candida/Candidiasis'), ('19', 'Cold/Common cold'),
                 ('20', 'Cough'), ('21', 'diarrhoea, gastroenteritis'),
                 ('22', 'epigastric pain'), ('23', 'fever'), ('24', 'ear infection'),
                 ('25', 'eye infection'), ('26', 'fibroids'),
                 ('27', 'warts/genital warts/vulvar warts/anal warts'),
                 ('28', 'headache'), ('29', 'heartburn'), ('30', 'hyperemesis'),
                 ('31', 'PID (pelvic inflammatory disease)'), ('32', 'Rash'),
                 ('33', 'Respiratory tract infection/URTI (upper resp tract infection)'),
                 ('34', 'sore throat/tonsillitis'),
                 ('35', 'psychiatric/mental disorders'), ('36', 'Assault/Trauma'),
                 ('37', 'Epilepsy/Seizures'), ('38', 'Scorpion stings/bites'),
                 ('39', 'Parasites/Intestinal worms'), ('40', 'Fungal Infection'),
                 ('41', 'Gastritis/Peptic Ulcer/Abdominal Ulcer'), ('42', 'Cancer'),
                 ('43', 'DVT'), ('44', 'Bronchitis'), ('45', 'Pneumonia'),
                 ('46', 'Epistaxis (bleeding from the nose)'), ('47', 'Hypotension'),
                 ('48', 'Cyst'), ('49', 'Abdominal Pain'), ('50', 'Backache/Waist ache'),
                 ('51', 'altered comfort/pain'), ('8', 'Other'), ('0', 'None'),
                 ('99', 'Unknown')),
        help_text="Check All that Apply", )

    otherdiagname = models.CharField(
        verbose_name="If other maternal diagnosis, specify:",
        max_length=100,
        help_text="", )

    tb_treatment = models.CharField(
        verbose_name="Is there documentation that this patient received anti-TB treatment (sometimes called \"ATT\" or \"HRZE\")",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    tbtreat_date = models.DateField(
        verbose_name="When did TB treatment start?",
        help_text="If unknown leave blank", )

    tb_meds = models.CharField(
        verbose_name="Which medications were used to treat TB? ",
        max_length=2,
        choices=(('1', 'INH (Isoniazid, the "H" in HRZE)'),
                 ('2', 'Rifampin (Rif, the "R" in HRZE)'),
                 ('3', 'Pyrazinamide (PZA, the "Z" in HRZE)'),
                 ('4', 'Ethambutol (the "E" in HRZE)'),
                 ('5', 'Streptomycin (this is given as an IV or IM)'), ('7', 'Rifabutin'),
                 ('8', 'Amikacin'), ('10', 'Levofloxacin'), ('9', 'Unknown')),
        help_text="Choose All that Apply", )

    iron = models.CharField(
        verbose_name="Was the patient taking iron (ferrous, ferrous sulfate, feS04)?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    vitaminc = models.CharField(
        verbose_name="Was the patient taking Vitamin C (ascorbic acid)?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    multivit = models.CharField(
        verbose_name="Was the patient taking a Multivitamin (MVI)?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    folate = models.CharField(
        verbose_name="Was the patient taking folate (folic acid)?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    fefol = models.CharField(
        verbose_name="Was the patient taking Iron with Folate (Ferrous with Folate/ FeFol)?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="This is a combination pill that contains both iron and folate", )

    datevitamin = models.DateField(
        verbose_name="If patient taking multivitamin or folate or FeFol(ferrous with folic), date the first one started",
        blank=True, null=True,
        help_text="MM - DD - YY   If UNKNOWN, Leave BLANK", )

    vitamindateunkown = models.CharField(
        verbose_name="Is the start date of multivitamin or folate UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    anti_malarials = models.CharField(
        verbose_name="Did this patient receive Anti-Malaria medicine in pregnancy?(either to treat malaria or for malaria prophylaxis/ prevention)treatment usually COARTEM or QUINIDINEprophylaxis usually CHLOROQUINE or Atovaquone/Proguanil",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No'), ('2', 'Unknown')),
        help_text="", )

    malaria_med = models.CharField(
        verbose_name="Which anti-malaria medications did this woman receive? ",
        max_length=1,
        choices=(('1', 'Chloroquine'), ('2', 'Atovaquone/Proguanil (Malarone)'),
                 ('3', 'Coartem (arthemether lumefantrine)'), ('4', 'Quinidine'),
                 ('5', 'Other')),
        help_text="Choose All that Apply", )

    other_mal_med = models.TextField(
        verbose_name="Other anti-malaria medication, please specify",
        help_text="", )

    chloroq_start = models.DateField(
        verbose_name="Cloroquine start date?",
        help_text="If unknown leave blank", )

    chloroq_start_unknown = models.CharField(
        verbose_name="Is cloroquine start date unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    chlor_ongoing = models.CharField(
        verbose_name="Is Chloroquine ongoing?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No'), ('2', 'Unknown')),
        help_text="", )

    chloroq_days = models.DecimalField(
        verbose_name="How many days was chloroquine taken?",
        decimal_places=2, max_digits=8,
        help_text="If unknown leave blank", )

    chloroq_days_unknown = models.CharField(
        verbose_name="Is it unknown how many days Chloroquine was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        blank=True, null=True,
        help_text="", )

    malarone_date = models.DateField(
        verbose_name="Atovaquone/Proguanil start date?",
        help_text="If unknown leave blank", )

    malarone_date_unknown = models.CharField(
        verbose_name="Is Atovaquone/Proguanil start date unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    malarone_ongoing = models.CharField(
        verbose_name="Is Atovaquone/Proguanil ongoing?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No'), ('2', 'Unknown')),
        help_text="", )

    malarone_days = models.DecimalField(
        verbose_name="How many days was atovaquone/proguanil taken?",
        decimal_places=2, max_digits=8,
        help_text="If unknown leave blank", )

    malarone_days_unknown = models.CharField(
        verbose_name="Is it unknown how many days Atovaquone/Proguanil was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    coartem_date = models.DateField(
        verbose_name="Coartem start date?",
        help_text="If unknown leave blank", )

    coartem_date_unknown = models.CharField(
        verbose_name="Is Coartem start date unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    coartem_ongoing = models.CharField(
        verbose_name="Is Co-Artem ongoing?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No'), ('2', 'Unknown')),
        help_text="", )

    coartem_days = models.DecimalField(
        verbose_name="How many days was Coartem taken?",
        decimal_places=2, max_digits=8,
        help_text="If unknown leave blank", )

    coartem_days_unknown = models.CharField(
        verbose_name="Is it unknown how many days Coartem was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    quin_date = models.DateField(
        verbose_name="Quinidine start date?",
        help_text="If unknown leave blank", )

    quin_date_unknown = models.CharField(
        verbose_name="Is quinidine start date unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    quin_days = models.DecimalField(
        verbose_name="How many days was quinidine taken?",
        decimal_places=2, max_digits=8,
        help_text="If unknown leave blank", )

    quin_days_unknown = models.CharField(
        verbose_name="Is it unknown how many days quinidine was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    other_mal_date = models.DateField(
        verbose_name="Other anti-malarial start date?",
        help_text="If unknown leave blank", )

    other_mal_date_unknown = models.CharField(
        verbose_name="Is other anti-malarial start date unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    othermal_ongoing = models.CharField(
        verbose_name="Is other anti-malarial ongoing?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No'), ('2', 'Unknown')),
        help_text="", )

    other_mal_days = models.DecimalField(
        verbose_name="How many days was other anti-malaria medication taken?",
        decimal_places=2, max_digits=8,
        help_text="If unknown leave blank", )

    other_mal_days_unknown = models.CharField(
        verbose_name="Is it unknown how many days other malarial was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    anymatabx = models.CharField(
        verbose_name="Did the patient receive antibiotics during pregnancy?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    abxspecify = models.CharField(
        verbose_name="Which Antibiotics did the patient take?",
        max_length=2,
        choices=(('1', 'Ceftriaxone'), ('2', 'Erythromycin'), ('10', 'Azithromycin'),
                 ('3', 'Metronidazole'), ('4', 'Amoxicillin'), ('5', 'Doxycycline'),
                 ('6', 'Penicillin'), ('7', 'Cloxacillin'), ('8', 'Cotrimoxazole (CTX)'),
                 ('9', 'Fluconazole'), ('14', 'Other')),
        blank=True, null=True,
        help_text="Check All that Apply", )

    otherabxname = models.CharField(
        verbose_name="Specify Other Antibiotic:",
        max_length=100,
        help_text="", )

    otherstart1 = models.DateField(
        verbose_name="Other Antibiotic Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    otherabxstartunknown = models.CharField(
        verbose_name="Is the Start Date for Other Antibiotic Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    otherdays = models.PositiveIntegerField(
        verbose_name="How many days was this OTHER antibiotic taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    otherabxdaysunknown = models.CharField(
        verbose_name="Is it unknown how long this OTHER antibiotic was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    azithrostart1 = models.DateField(
        verbose_name="Azithromycin Start Date:",
        help_text="If UNKNOWN, Leave BLANK", )

    azithrodateunknown = models.CharField(
        verbose_name="Is the Start Date for Azithromycin Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Ceftriaxone date is known, please go back and enter it", )

    azithrodays1 = models.PositiveIntegerField(
        verbose_name="How many days was Azithromycin taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    azithrodaysunknown1 = models.CharField(
        verbose_name="Is it unknown how long Azithromycin was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    ceftriaxstart1 = models.DateField(
        verbose_name="Ceftriaxone Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    ceftriaxdateunknown = models.CharField(
        verbose_name="Is the Start Date for Ceftriaxone Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Ceftriaxone date is known, please go back and enter it", )

    ceftriaxdays1 = models.PositiveIntegerField(
        verbose_name="How many days was Ceftriaxone taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    ceftriaxdaysunknown = models.CharField(
        verbose_name="Is it unknown how long Ceftriaxone was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    erythrostart1 = models.DateField(
        verbose_name="Erythromycin Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    erythrostartunknown = models.CharField(
        verbose_name="Is the Start Date for Erythromycin Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Erythromycin date is known, please go back and enter it", )

    erythrodays1 = models.PositiveIntegerField(
        verbose_name="How many days was Erythromycin taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    erythrodaysunknown = models.CharField(
        verbose_name="Is it unknown how long Erythromycin was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    metrostart1 = models.DateField(
        verbose_name="Metronidazole Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    metrostartunknown = models.CharField(
        verbose_name="Is the Start Date for Metronidazole Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Metronidazole date is known, please go back and enter it", )

    metrodays1 = models.PositiveIntegerField(
        verbose_name="How many days was Metronidazole taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    metrodaysunknown = models.CharField(
        verbose_name="Is it unknown how long Metronidazole was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    amoxstart1 = models.DateField(
        verbose_name="Amoxicillin Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    amoxstartunknown = models.CharField(
        verbose_name="Is the Start Date for Amoxicillin Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Amoxicillin date is known, please go back and enter it", )

    amoxdays1 = models.PositiveIntegerField(
        verbose_name="How many days was Amoxicillin taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    amoxdaysunknown = models.CharField(
        verbose_name="Is it unknown how long Amoxicillin was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    doxystart1 = models.DateField(
        verbose_name="Doxycycline Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    doxystartunknown = models.CharField(
        verbose_name="Is the Start Date for Doxycycline Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Doxycycline date is known, please go back and enter it", )

    doxydays1 = models.PositiveIntegerField(
        verbose_name="How many days was Doxycycline taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    doxydaysunknown = models.CharField(
        verbose_name="Is it unknown how long Doxycycline was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    penicilstart1 = models.DateField(
        verbose_name="Penicillin Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    penicilstartunknown = models.CharField(
        verbose_name="Is the Start Date for Penicillin Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Penicillin date is known, please go back and enter it", )

    penicildays1 = models.PositiveIntegerField(
        verbose_name="How many days was Penicillin taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    penicildaysunknown = models.CharField(
        verbose_name="Is it unknown how long Penicillin was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    cloxstart1 = models.DateField(
        verbose_name="Cloxacillin Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    cloxstartunknown = models.CharField(
        verbose_name="Is the Start Date for Cloxacillin Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Cloxacillin date is known, please go back and enter it", )

    cloxdays1 = models.PositiveIntegerField(
        verbose_name="How many days was Cloxacillin taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    cloxdaysunknown = models.CharField(
        verbose_name="Is it unknown how long Cloxacillin was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    cotristart1 = models.DateField(
        verbose_name="Cotrimoxazole Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    cotristartunknown = models.CharField(
        verbose_name="Is the Start Date for Cotrimoxazole Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Cotrimoxazole date is known, please go back and enter it", )

    cotriprior = models.CharField(
        verbose_name="Was Cotrimoxazole Started Prior to Conception?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="This question only applies if Cotrimoxazole Start Date is Unknown", )

    cotridays1 = models.PositiveIntegerField(
        verbose_name="How many days was Cotrimoxazole taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    cotridaysunknown = models.CharField(
        verbose_name="Is it unknown how long Cotrimoxazole was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    flucstart1 = models.DateField(
        verbose_name="Fluconazole Start Date:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    flucstartunknown = models.CharField(
        verbose_name="Is the Start Date for Fluconazole Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Fluconazole date is known, please go back and enter it", )

    flucprior = models.CharField(
        verbose_name="Was Fluconazole Started Prior to Conception?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="This question only applies if Flucazole Start Date is Unknown", )

    flucdays1 = models.PositiveIntegerField(
        verbose_name="How many days was Fluconazole taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    flucdaysunknown = models.CharField(
        verbose_name="Is it unknown how long Fluconazole was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    otherabx2 = models.CharField(
        verbose_name="Was an OTHER antibiotic taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    otherstart2 = models.DateField(
        verbose_name="Other Antibiotic Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    otherabxstartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Other Antibiotic (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    otherabxdays2 = models.PositiveIntegerField(
        verbose_name="How many days was this OTHER antibiotic (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    otherabxdaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long this OTHER antibiotic (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    azithro2 = models.CharField(
        verbose_name="Was Azithromycin taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    azithrostart2 = models.DateField(
        verbose_name="Azithromycin Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    azithrodateunknown2 = models.CharField(
        verbose_name="Is the Start Date for Azithromycin (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Ceftriaxone date is known, please go back and enter it", )

    azithrodays2 = models.PositiveIntegerField(
        verbose_name="How many days was Azithromycin (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    azithrodaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Azithro (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    ceftriax2 = models.CharField(
        verbose_name="Was Ceftriaxone taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    ceftriaxstart2 = models.DateField(
        verbose_name="Ceftriaxone Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    ceftriaxdateunknown2 = models.CharField(
        verbose_name="Is the Start Date for Ceftriaxone (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Ceftriaxone date is known, please go back and enter it", )

    ceftriaxdays2 = models.PositiveIntegerField(
        verbose_name="How many days was Ceftriaxone (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    ceftriaxdaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Ceftriaxone (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    ceftriax3 = models.CharField(
        verbose_name="Was Ceftriaxone taken for a third time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    ceftriaxstart3 = models.DateField(
        verbose_name="Ceftriaxone Start Date (3rd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    ceftriax3dateunknown = models.CharField(
        verbose_name="Is the Start Date for Ceftriaxone (3rd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        blank=True, null=True,
        help_text="If Ceftriaxone date is known, please go back and enter it", )

    ceftriaxdays3 = models.PositiveIntegerField(
        verbose_name="How many days was Ceftriaxone (3rd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    ceftriaxdaysunknown3 = models.CharField(
        verbose_name="Is it unknown how long Ceftriaxone (3rd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    erythro2 = models.CharField(
        verbose_name="Was Erythromycin taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    erythrostart2 = models.DateField(
        verbose_name="Erythromycin Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    erythrostartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Erythromycin (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Erythromycin date is known, please go back and enter it", )

    erythrodays2 = models.PositiveIntegerField(
        verbose_name="How many days was Erythromycin (2nd course)  taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    erythrodaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Erythromycin (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    metro2 = models.CharField(
        verbose_name="Was Metronidazole taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    metrostart2 = models.DateField(
        verbose_name="Metronidazole Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    metrostartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Metronidazole (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Metronidazole date is known, please go back and enter it", )

    metrodays2 = models.PositiveIntegerField(
        verbose_name="How many days was Metronidazole (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    metrodaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Metronidazole (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    amox2 = models.CharField(
        verbose_name="Was Amoxicillin taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    amoxstart2 = models.DateField(
        verbose_name="Amoxicillin Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    amoxstartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Amoxicillin (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Amoxicillin date is known, please go back and enter it", )

    amoxdays2 = models.PositiveIntegerField(
        verbose_name="How many days was Amoxicillin (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    amoxdaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Amoxicillin (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    doxy2 = models.CharField(
        verbose_name="Was Doxycycline taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    doxystart2 = models.DateField(
        verbose_name="Doxycycline Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    doxystartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Doxycycline (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Doxycycline date is known, please go back and enter it", )

    doxydays2 = models.PositiveIntegerField(
        verbose_name="How many days was Doxycycline (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    doxydaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Doxycycline (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    penicil2 = models.CharField(
        verbose_name="Was Penicillin taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'No')),
        help_text="", )

    penicilstart2 = models.DateField(
        verbose_name="Penicillin Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    penicilstartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Penicillin (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Penicillin date is known, please go back and enter it", )

    penicildays2 = models.PositiveIntegerField(
        verbose_name="How many days was Penicillin (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    penicildaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Penicillin (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    clox2 = models.CharField(
        verbose_name="Was Cloxacillin taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    cloxstart2 = models.DateField(
        verbose_name="Cloxacillin Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    cloxstartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Cloxacillin (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Cloxacillin date is known, please go back and enter it", )

    cloxdays2 = models.PositiveIntegerField(
        verbose_name="How many days was Cloxacillin (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    cloxdaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Cloxacillin (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    cotri2 = models.CharField(
        verbose_name="Was Cotrimoxazole taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    cotristart2 = models.DateField(
        verbose_name="Cotrimoxazole Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    cotristartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Cotrimoxazole (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Cotrimoxazole date is known, please go back and enter it", )

    cotridays2 = models.PositiveIntegerField(
        verbose_name="How many days was Cotrimoxazole (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    cotridaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Cotrimoxazole (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    fluc2 = models.CharField(
        verbose_name="Was Fluconazole taken for a second time during this pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    flucstart2 = models.DateField(
        verbose_name="Fluconazole Start Date (2nd course):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    flucstartunknown2 = models.CharField(
        verbose_name="Is the Start Date for Fluconazole (2nd course) Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="If Fluconazole date is known, please go back and enter it", )

    flucdays2 = models.PositiveIntegerField(
        verbose_name="How many days was Fluconazole (2nd course) taken?",
        blank=True, null=True,
        help_text="If unknown, LEAVE BLANK", )

    flucdaysunknown2 = models.CharField(
        verbose_name="Is it unknown how long Fluconazole (2nd course) was taken?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    commentabx = models.TextField(
        verbose_name="Antibiotic Comments: (for example, if more than 1 unknown antibiotic was taken can specify the other antibiotic.  Or if more than 2 courses of an anitbiotic was taken during pregnancy can specify antibiotic antibiotic, date and number of days taken)",
        blank=True, null=True,
        help_text="", )

    arv_hivneg = models.CharField(
        verbose_name="Did the patient receive any antiretroviral medications (ARVs) during pregnancy?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    arv_hivneg_reg = models.CharField(
        verbose_name="Which antiretrovirals (ARVs) did the patient receive during pregnancy? (choose all that apply)",
        max_length=1,
        choices=(('1',
                  'TDF/FTC (truvada, TDF/emtricitabine, tenofovir disproxil fumarate/emtricitabine)'),
                 ('2',
                  'TAF/FTC (descovy, TAF/emtricitabine, tenofovir alafenaminde/emtricitabine)'),
                 ('3', 'TLD (truvada/lamivudine/dolutegravir)'),
                 ('4', 'cabotegravir injectible (CAB-LA, CAB)'), ('6', 'Unspecified'),
                 ('5', 'other')),
        help_text="", )

    arv_hivneg_other = models.CharField(
        verbose_name="What other antiretrovirals did this patient receive? Please specify",
        max_length=100,
        help_text="", )

    arv_hivneg_truvconcept = models.CharField(
        verbose_name="Was TDF/FTC started prior to conception?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'No'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_tafconcept = models.CharField(
        verbose_name="Was TAF/FTC started prior to conception?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'No'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_tldconcept = models.CharField(
        verbose_name="Was TLD started prior to conception?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'No'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_cabconcept = models.CharField(
        verbose_name="Was cabotegravir started prior to conception?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_unspeconcept = models.CharField(
        verbose_name="Was unspecified PrEP started prior to conception?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_otherconcept = models.CharField(
        verbose_name="Were Other ARVs started prior to conception?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'No'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_truvdelivery = models.CharField(
        verbose_name="Was TDF/FTC continued through delivery? (still on TDF/FTC when admitted for delivery)",
        max_length=2,
        choices=(('1', 'YES'), ('2', 'NO'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_tafdelivery = models.CharField(
        verbose_name="Was TAF/FTC continued through delivery? (still on TAF/FTC when admitted for delivery)",
        max_length=2,
        choices=(('1', 'YES'), ('2', 'NO'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_tlddelivery = models.CharField(
        verbose_name="Was TLD continued through delivery? (still on TLD when admitted for delivery)",
        max_length=2,
        choices=(('1', 'YES'), ('2', 'NO'), ('99', 'unknown')),
        blank=True, null=True,
        help_text="", )

    arv_hivneg_cabdelivery = models.CharField(
        verbose_name="Was cabotegravir continued through delivery? (still on CAB when admitted for delivery)",
        max_length=2,
        choices=(('1', 'YES'), ('2', 'NO'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_unspedelivery = models.CharField(
        verbose_name="Was unspecified PrEP continued through delivery? (still on CAB when admitted for delivery)",
        max_length=2,
        choices=(('1', 'YES'), ('2', 'NO'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_otherdelivery = models.CharField(
        verbose_name="Were the Other ARVs continued through delivery? (still on Other ARVs when admitted for delivery)",
        max_length=2,
        choices=(('1', 'YES'), ('2', 'NO'), ('99', 'unknown')),
        help_text="", )

    arv_hivneg_truvstart = models.DateField(
        verbose_name="What was the start date for TDF/FTC?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_tafstart = models.DateField(
        verbose_name="What was the start date for TAF/FTC?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_tldstart = models.DateField(
        verbose_name="What was the start date for TLD?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_cabstart = models.DateField(
        verbose_name="What was the start date for cabotegtavir?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_unspestart = models.DateField(
        verbose_name="What was the start date for unspecified PrEP?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_otherstart = models.DateField(
        verbose_name="What was the start date for other ARVs?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_truvstartunk = models.CharField(
        verbose_name="Is the start date for TDF/FTC unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    arv_hivneg_tafstartunk = models.CharField(
        verbose_name="Is the start date for TAF/FTC unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    arv_hivneg_tldstartunk = models.CharField(
        verbose_name="Is the start date for TLD unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    arv_hivneg_cabstartunk = models.CharField(
        verbose_name="Is the start date for cabotegravir unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        blank=True, null=True,
        help_text="", )

    arv_hivneg_unspestartunk = models.CharField(
        verbose_name="Is the start date for unspecified PrEP unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        blank=True, null=True,
        help_text="", )

    arv_hivneg_otherstartunk = models.CharField(
        verbose_name="Is the start date for Other ARVs unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        blank=True, null=True,
        help_text="", )

    arv_hivneg_truvstop = models.DateField(
        verbose_name="What was the stop date for TDF/FTC?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_tafstop = models.DateField(
        verbose_name="What was the stop date for TAF/FTC?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_tldstop = models.DateField(
        verbose_name="What was the stop date for TLD?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_cabstop = models.DateField(
        verbose_name="What was the stop date for cabotegravir?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_unspestop = models.DateField(
        verbose_name="What was the stop date for unspecified PrEP?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_otherstop = models.DateField(
        verbose_name="What was the stop date for Other ARVs?",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    arv_hivneg_truvstopunk = models.CharField(
        verbose_name="Is the stop date for TDF/FTC unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    arv_hivneg_tafstopunk = models.CharField(
        verbose_name="Is the stop date for TAF/FTC unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    arv_hivneg_tldstopunk = models.CharField(
        verbose_name="Is the stop date for TLD unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    arv_hivneg_cabstopunk = models.CharField(
        verbose_name="Is the stop date for cabotegravir unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    arv_hivneg_unspestopunk = models.CharField(
        verbose_name="Is the stop date for unspecified PrEP unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    arv_hivneg_otherstopunk = models.CharField(
        verbose_name="Is the stop date for Other ARVs unknown?",
        max_length=1,
        choices=(('1', 'YES'),),
        help_text="", )

    covid_anytest = models.CharField(
        verbose_name="Did this woman have any documented COVID-19 test during pregnancy or while admitted to maternity (even after delivery)?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    covidsusp = models.CharField(
        verbose_name="Was this woman ever a COVID \"suspect\" but no test was ever done?",
        max_length=1,
        choices=(('1', 'YES'), ('2', 'NO')),
        help_text="", )

    covid_testnum = models.PositiveIntegerField(
        verbose_name="How many COVID tests did this mother have during pregnancy or while admitted to maternity (including after delivery)?",
        help_text="", )

    covidtest_date1 = models.DateField(
        verbose_name="Date of first COVID test ",
        help_text="If unknown leave blank", )

    covid_result1 = models.CharField(
        verbose_name="Result of first COVID test ",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminate'),
                 ('4', 'Still pending'), ('5', 'Unknown')),
        help_text="", )

    covidtest_date2 = models.DateField(
        verbose_name="Date of second COVID test ",
        help_text="If unknown leave blank", )

    covid_result2 = models.CharField(
        verbose_name="Result of second COVID test ",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminate'),
                 ('4', 'Still pending'), ('5', 'Unknown')),
        help_text="", )

    covidtest_date3 = models.DateField(
        verbose_name="Date of third COVID test ",
        help_text="If unknown leave blank", )

    covid_result3 = models.CharField(
        verbose_name="Result of third COVID test ",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminate'),
                 ('4', 'Still pending'), ('5', 'Unknown')),
        help_text="", )

    covidtest_date4 = models.DateField(
        verbose_name="Date of fourth COVID test ",
        help_text="", )

    covid_result4 = models.CharField(
        verbose_name="Result of fourth COVID test ",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminate'),
                 ('4', 'Still pending'), ('5', 'Unknown')),
        help_text="", )

    covidtest_date5 = models.DateField(
        verbose_name="Date of fifth COVID test ",
        help_text="If unknown leave blank", )

    covid_result5 = models.CharField(
        verbose_name="Result of fifth COVID test ",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminate'),
                 ('4', 'Still pending'), ('5', 'Unknown')),
        help_text="", )

    covidtest_date6 = models.DateField(
        verbose_name="Date of sixth COVID test ",
        help_text="If unknown leave blank", )

    covid_result6 = models.CharField(
        verbose_name="Result of sixth COVID test ",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminate'),
                 ('4', 'Still pending'), ('5', 'Unknown')),
        help_text="", )

    covid_testinfant = models.CharField(
        verbose_name="Did the infant receive a COVID test?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    covid_testresult_infant = models.CharField(
        verbose_name="Result of Infant COVID test",
        max_length=1,
        choices=(('1', 'Positive'), ('2', 'Negative'), ('3', 'Indeterminate'),
                 ('4', 'Still pending'), ('5', 'Unknown')),
        help_text="", )

    mother_covidicu = models.CharField(
        verbose_name="Was the mother every admitted to the ICU during this admission?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    mother_covidoutcome = models.CharField(
        verbose_name="At the time of discharge of the baby, what was the disposition of the mother?",
        max_length=1,
        choices=(('1', 'Mother Died'), ('2', 'Mother Remains hospitalized'),
                 ('3', 'Mother Transferred to another hospital'),
                 ('4', 'Mother Discharged Alive')),
        help_text="", )

    maternal_coviddeathdate = models.DateField(
        verbose_name="Date of Death (mother)",
        help_text="", )

    maternal_coviddeathcause = models.TextField(
        verbose_name="Cause of Death (mother)",
        help_text="", )

    maternal_covidtransferhosp = models.CharField(
        verbose_name="Which hospital was she transferred to?",
        max_length=1,
        choices=(
        ('1', 'PMH'), ('2', 'NRH'), ('3', 'University of Botswana Academic hospital'),
        ('4', 'Gabs Private'), ('5', 'Bokamoso'), ('6', 'Other Private hospital'),
        ('7', 'South African hospital'), ('8', 'Unknown')),
        help_text="", )

    covid_comments = models.TextField(
        verbose_name="Additional comments on COVID: please include a description of what happened to the mother, describe anything about testing that is not clear, or any other details that can't be captured in the other questions",
        blank=True, null=True,
        help_text="", )

    delivdate = models.DateField(
        verbose_name="Delivery Date:",
        help_text="", )

    deliv_method = models.CharField(
        verbose_name="Method of Delivery",
        max_length=1,
        choices=(
        ('1', 'SVD (spontaneous vaginal delivery)'), ('2', 'Breech'), ('3', 'Vacuum'),
        ('4', 'C/S (C-section)'), ('6', 'Forceps delivery'), ('5', 'Unknown')),
        help_text="", )

    sched_cs = models.CharField(
        verbose_name="Was this a scheduled C-section? (the woman came to the hospital on this specified date because she was known to need a C-section prior to delivery.  This can happen, for example, if she has required multiple C-sections in the past.",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'UNKNOWN')),
        blank=True, null=True,
        help_text="", )

    induced = models.CharField(
        verbose_name="Was labor induced?",
        max_length=2,
        choices=(('1', 'YES'), ('0', 'NO'), ('99', 'Unknown')),
        help_text="", )

    azt_labor = models.CharField(
        verbose_name="Is there DOCUMENTATION that the mother received AZT during labor?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    nvp_labor = models.CharField(
        verbose_name="Is there DOCUMENTATION that the mother received NVP (Nevirapine) during labor?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        blank=True, null=True,
        help_text="", )

    infant_nvp = models.CharField(
        verbose_name="Is there DOCUMENTATION that the infant received nevirapine after delivery?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    numdeliv = models.PositiveIntegerField(
        verbose_name="Number of Infants Delivered: ",
        help_text="If 4 or more babies delivered please enter 4", )

    infantstat = models.CharField(
        verbose_name="Infant Status:",
        max_length=2,
        choices=(('1', 'Alive'), ('2', 'FSB'), ('3', 'MSB'), ('99', 'UNKNOWN')),
        help_text="FSB=Fresh Stillbirth MSB=Macerated Stillbirth", )

    nndeath = models.CharField(
        verbose_name="Neonatal Death (<28 days)?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    nndeath_twin = models.CharField(
        verbose_name="Neonatal Death (< 28 days) of second twin?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    nndeath_triplet = models.CharField(
        verbose_name="Neonatal Death (< 28 days) of triplet (third born of triplets?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        blank=True, null=True,
        help_text="", )

    nndeath_quad = models.CharField(
        verbose_name="Neonatal Death (< 28 days) of quadruplet (last born of four)?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    nndeath_date = models.DateField(
        verbose_name="Date of neonatal death?",
        blank=True, null=True,
        help_text="", )

    nndeath_date_twin = models.DateField(
        verbose_name="Date of neonatal death of twin?",
        blank=True, null=True,
        help_text="", )

    nndeath_date_triplet = models.DateField(
        verbose_name="Date of neonatal death of triplet?",
        blank=True, null=True,
        help_text="", )

    nndeath_date_quad = models.DateField(
        verbose_name="Date of neonatal death of quadruplet?",
        blank=True, null=True,
        help_text="", )

    nndeath_date_unk = models.CharField(
        verbose_name="Is Neonatal Death Date unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    nndeath_date_unk_twin = models.CharField(
        verbose_name="Is Neonatal Death Date of twin unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    nndeath_date_unk_triplet = models.CharField(
        verbose_name="Is Neonatal Death Date of triplet unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    nndeath_date_unk_quad = models.CharField(
        verbose_name="Is Neonatal Death Date of quadruplet unknown?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    nndcause = models.TextField(
        verbose_name="Cause of death (list all reasons):",
        help_text="", )

    nga = models.PositiveIntegerField(
        verbose_name="Gestation by ANC (in weeks):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    ngaunknown = models.CharField(
        verbose_name="Is Gestational age UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    gender = models.CharField(
        verbose_name="Gender:",
        max_length=2,
        choices=(('0', 'Male'), ('1', 'Female'),
                 ('2', 'Ambiguous (characteristics of both male and female)'),
                 ('99', 'UNKNOWN')),
        help_text="", )

    gender_twin = models.CharField(
        verbose_name="Gender of twin (second born):",
        max_length=2,
        choices=(('0', 'Male'), ('1', 'Female'),
                 ('2', 'Ambiguous (characteristics of both male and female)'),
                 ('99', 'UNKNOWN')),
        help_text="", )

    gender_triplet = models.CharField(
        verbose_name="Gender of triplet (third born):",
        max_length=2,
        choices=(('0', 'Male'), ('1', 'Female'),
                 ('2', 'Ambiguous (characteristics of both male and female)'),
                 ('99', 'UNKNOWN')),
        help_text="", )

    gender_quad = models.CharField(
        verbose_name="Gender of quadruplet (fourth born):",
        max_length=2,
        choices=(('0', 'Male'), ('1', 'Female'),
                 ('2', 'Ambiguous (characteristics of both male and female)'),
                 ('99', 'UNKNOWN')),
        help_text="", )

    bwt = models.PositiveIntegerField(
        verbose_name="Birthweight (grams):",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    bwtunknown = models.CharField(
        verbose_name="Is birthweight UNKNOWN?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    infant_length = models.DecimalField(
        verbose_name="Infant Length (centimeters)",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    length_unknown = models.CharField(
        verbose_name="Is Infant Length Unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        help_text="", )

    headcirc = models.DecimalField(
        verbose_name="Infant Head Circumference (centimeters)",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    headcirc_unknown = models.CharField(
        verbose_name="Is infant head circumference unknown?",
        max_length=1,
        choices=(('1', 'Yes'),),
        blank=True, null=True,
        help_text="", )

    apgar1 = models.CharField(
        verbose_name="Total Apgar Score at 1 minute?",
        max_length=2,
        choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                 ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
                 ('11', 'UNKNOWN')),
        help_text="", )

    apgar5 = models.CharField(
        verbose_name="Total Apgar Score at 5 minutes?",
        max_length=2,
        choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                 ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
                 ('11', 'UNKNOWN')),
        help_text="", )

    apgar10 = models.CharField(
        verbose_name="Total Apgar Score at 10 minutes?",
        max_length=2,
        choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                 ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
                 ('11', 'UNKNOWN')),
        help_text="", )

    congenabn = models.CharField(
        verbose_name="Documentation of Congenital abnormalities?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    twin = models.CharField(
        verbose_name="Status of the SECOND infant at delivery:",
        max_length=2,
        choices=(('1', 'Alive'), ('2', 'FSB'), ('3', 'MSB'), ('99', 'UNKNOWN')),
        help_text="", )

    bwt_twin = models.PositiveIntegerField(
        verbose_name="Birthweight (grams) of second infant:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    length_twin = models.PositiveIntegerField(
        verbose_name="Length (cm) of second infant:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    headcirc_twin = models.DecimalField(
        verbose_name="Infant Head Circumference of second infant (centimeters)",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    twinca = models.CharField(
        verbose_name="Did the SECOND infant have any congenital abnormalities?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    triplet = models.CharField(
        verbose_name="Status of the THIRD infant at delivery:",
        max_length=2,
        choices=(('1', 'Alive'), ('2', 'FSB'), ('3', 'MSB'), ('99', 'UNKNOWN')),
        help_text="", )

    bwt_triplet = models.PositiveIntegerField(
        verbose_name="Birthweight (grams) of third infant:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    length_triplet = models.PositiveIntegerField(
        verbose_name="Length (cm) of third infant:",
        blank=True, null=True,
        help_text="If UNKNOWN, Leave BLANK", )

    headcirc_triplet = models.DecimalField(
        verbose_name="Infant Head Circumference of third infant (centimeters)",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="If UNKNOWN, Leave Blank", )

    tripletca = models.CharField(
        verbose_name="Did the THIRD infant have any congenital abnormalities?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    quad = models.CharField(
        verbose_name="Status of the FOURTH infant at delivery:",
        max_length=2,
        choices=(('1', 'Alive'), ('2', 'FSB'), ('3', 'MSB'), ('99', 'UNKNOWN')),
        help_text="", )

    bwt_quad = models.PositiveIntegerField(
        verbose_name="Birthweight (grams) of fourth infant:",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    length_quad = models.PositiveIntegerField(
        verbose_name="Length (cm) of fourth infant:",
        blank=True, null=True,
        help_text="If unknown leave blank", )

    headcirc_quad = models.DecimalField(
        verbose_name="Infant Head Circumference of fourth infant (centimeters)",
        decimal_places=2, max_digits=8,
        blank=True, null=True,
        help_text="If unknown leave blank", )

    quadca = models.CharField(
        verbose_name="Did the FOURTH infant have any congenital abnormalities?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    alivebaby = models.CharField(
        verbose_name="Neonate Alive at Discharge?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    alivebaby_twin = models.CharField(
        verbose_name="Twin Alive at Discharge?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    alivebaby_triplet = models.CharField(
        verbose_name="Triplet Alive at Discharge?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    infant_death = models.CharField(
        verbose_name="Did this infant die at >28 days old?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    infant_death_twin = models.CharField(
        verbose_name="Did this twin die at >28 days old?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    infant_death_triplet = models.CharField(
        verbose_name="Did this triplet die at >28 days old?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    nnu = models.CharField(
        verbose_name="Neonate Required NNU?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    nnu_twin = models.CharField(
        verbose_name="Twin Required NNU?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    nnu_triplet = models.CharField(
        verbose_name="Triplet Required NNU?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'Unknown')),
        help_text="", )

    reasonnnu = models.TextField(
        verbose_name="Reason(s) neonate required NNU (list all):",
        help_text="", )

    reasonnnu_twin = models.TextField(
        verbose_name="Reason(s) twin required NNU (list all):",
        help_text="", )

    reasonnnu_triplet = models.TextField(
        verbose_name="Reason(s) triplet required NNU (list all):",
        help_text="", )

    feeding = models.CharField(
        verbose_name="Feeding Choice (according to what is written in the MATERNITY CARD)",
        max_length=2,
        choices=(('1', 'Breastfeeding (BF or EBF)'), ('0', 'Formula Feeding (FF or EFF)'),
                 ('99', 'UNKNOWN')),
        help_text="", )

    feeding2 = models.CharField(
        verbose_name="What is the feeding choice? (according to PMTCT counsellor, formula log, direct observation or HIV data abstraction sheet)",
        max_length=1,
        choices=(
        ('1', 'Breastfeeding (BF)'), ('2', 'Formula Feeding (FF)'), ('3', 'Unknown')),
        help_text="only for HIV-positives", )

    feedingsource = models.CharField(
        verbose_name="Did you get this feeding information from (choose all that apply):",
        max_length=1,
        choices=(('1', 'Formula log'),
                 ('2', 'Verbal confirmation from PMTCT or feeding counsellor'),
                 ('3', 'Direct observation of the mom'),
                 ('4', 'HIV Data abstraction form')),
        help_text="only for HIV-positives", )

    jaundice = models.CharField(
        verbose_name="Documentation of neonatal jaundice?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    eit = models.CharField(
        verbose_name="Was this infant screened for the EIT study?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    eit_bid = models.CharField(
        verbose_name="What is the EIT screening BID?",
        max_length=100,
        help_text="Should look like \"S-10-0001-91\"", )

    dorisduke = models.CharField(
        verbose_name="Was this mother enrolled in the Doris Duke Study?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    dorisduke_ptid = models.CharField(
        verbose_name="What is the Doris Duke PTID",
        max_length=100,
        blank=True, null=True,
        help_text="", )

    mechanisms = models.CharField(
        verbose_name="Was this mother enrolled in the mechanisms study (Rebecca's K23) ?  (if so the BID will be on the inside cover of the maternity card)",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    mechanism_bid = models.CharField(
        verbose_name="What is the Mechanisms Study BID?",
        max_length=100,
        help_text="", )

    ca_management = models.CharField(
        verbose_name="How was this infant's congenital abnormality managed? (check all that apply)",
        max_length=2,
        choices=(('1', 'Seen by an Medical Officer in the hospital'),
                 ('2', 'Seen by a Pediatrician in the hospital'),
                 ('9', 'Admitted to the NNU'),
                 ('3', 'Transferred directly to another hospital for further management'),
                 ('4', 'Referred to a pediatrician or specialist after discharge'),
                 ('5', 'Told to follow up at the local clinic after discharge'),
                 ('6', 'Told there was no need for any follow up for this abnormality'),
                 ('7', 'N/A because this was a stillbirth'),
                 ('8', 'N/A because this child died soon after birth'), ('99', 'Unknown'),
                 ('10', 'Other')),
        help_text="", )

    ca_managed_comment = models.TextField(
        verbose_name="How was this patient's congenital abnormality managed? Please use this box for any further clarification:",
        blank=True, null=True,
        help_text="", )

    attempt_consent = models.CharField(
        verbose_name="Was there an attempt to obtain consent for a photograph from the mother of the infant? ",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    noattempt_consent_reason = models.CharField(
        verbose_name="Why was there no attempt to consent? (choose all that apply)",
        max_length=1,
        choices=(('1', 'Nurse did not alert RA about the abnormality'),
                 ('2', 'Delivery happened at night/after working hours'),
                 ('3', 'Delivery happened on a weekend'), ('4',
                                                           'Delivery happened when RA was on leave, at a training or at a workshop'),
                 ('5', 'Mother left the hospital before consent was attempted'), ('7',
                                                                                  'This is not an abnormality that we are collecting (for example: birthmark, undescended testes, hernia)'),
                 ('6', 'Other')),
        help_text="", )

    other_noconsent = models.TextField(
        verbose_name="Please specify 'other' reason for not attempting consent",
        help_text="", )

    consent_obtained = models.CharField(
        verbose_name="Did the mother provide consent to take a photo of her infant?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    consent_underst = models.CharField(
        verbose_name="During the consent process, did the mother express understanding that the study does not provide any care or services for the child and that she should seek care for the child as recommended by the local health care providers and not wait for a result from our study?  ",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    future_photo_consent = models.CharField(
        verbose_name="Did the mother AGREE to allow the photo to be used for training and future publications?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    datetime_consent = models.DateTimeField(
        verbose_name="What was the date and time of Consent?",
        help_text="MM - DD - YY Hour:Minute", )

    ca_iccopy = models.CharField(
        verbose_name="Was the mother offered a copy of Tsepamo congenital abnormalities consent version 1.0?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    maternal_refusal_reason = models.TextField(
        verbose_name="What reason did the mother give for refusing consent to take a photo of her infant?",
        help_text="", )

    photo_taken = models.CharField(
        verbose_name="Was at least 1 photo taken of this infant?",
        max_length=1,
        choices=(('1', 'YES'), ('0', 'NO')),
        help_text="", )

    consent_received = models.CharField(
        verbose_name="Maternal Consent Form Received by Head Nurse in Gaborone?**TO BE FILLED BY HEAD NURSE, NOT RA",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    photo1 = models.FileField(
        verbose_name="Infant Photo 1",
        help_text="", )

    photo2 = models.FileField(
        verbose_name="Infant Photo 2",
        blank=True, null=True,
        help_text="not required, but some infants may need more than one photo to document all their abnormalities", )

    photo3 = models.FileField(
        verbose_name="Infant Photo 3",
        blank=True, null=True,
        help_text="not required, but some infants may need more than one photo to document all their abnormalities", )

    photo4 = models.FileField(
        verbose_name="Infant Photo 4",
        blank=True, null=True,
        help_text="not required, but some infants may need more than one photo to document all their abnormalities", )

    ca_photo_twin = models.FileField(
        verbose_name="Second Infant (twin) photo",
        help_text="", )

    ca_photo_triplet = models.FileField(
        verbose_name="Third Infant (triplet) photo",
        help_text="", )

    headneckdescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    ca_callslt = models.CharField(
        verbose_name="Did you call Modiegi (or if she isn't available, call Judith) to discuss the description of this abnormality?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    ca_desc_speak = models.CharField(
        verbose_name="Who did you speak to about the description of the abnormality?",
        max_length=1,
        choices=(('1', 'Modiegi'), ('2', 'Judith'), ('3', 'Mma Mayondi')),
        help_text="", )

    ca_notcall = models.CharField(
        verbose_name="Modiegi was not called because the abnormality was one of the following (choose one)--if abnormality is not on this list, you need to call Modiegi to discuss.",
        max_length=1,
        choices=(('1', 'Extra digit (soft, no bone, next to the 5th digit)'),
                 ('2', 'Umbilical Hernia'), ('3', 'Birthmark'),
                 ('4', 'Hyperextended leg'), ('5', 'Albino'),
                 ('6', 'Undecended testes (without any other abnormality)')),
        help_text="", )

    ca_description_twin = models.TextField(
        verbose_name="Description of Abnormality for Second infant born (twin): (please include as much detail as possible)",
        help_text="", )

    ca_description_triplet = models.TextField(
        verbose_name="Description of Abnormality for third infant born (triplet): (please include as much detail as possible)",
        help_text="", )

    extradigit = models.CharField(
        verbose_name="Is the abnormality an extra digit?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    extradigit_site = models.CharField(
        verbose_name="Where are the extra digits? (choose ALL that apply)",
        max_length=1,
        choices=(
        ('1', 'Left hand'), ('2', 'Right hand'), ('3', 'Left foot'), ('4', 'Right foot'),
        ('5', 'Unknown')),
        help_text="", )

    extra_digit_lhand = models.CharField(
        verbose_name="Where on the left hand is the extra digit located?",
        max_length=1,
        choices=(('1', 'Near the 5th digit (little finger, pinky finger)'),
                 ('2', 'Near the thumb'), ('3', 'Other place')),
        help_text="", )

    extradigit_lhand_bone = models.CharField(
        verbose_name="Does the extra digit appear as:",
        max_length=1,
        choices=(('1',
                  'A fullly formed extra digit (seems to look like a finger and have bone in it)'),
                 ('2', 'Soft, without a bone (sometimes hanging by a stalk)')),
        help_text="", )

    extra_digit_rhand = models.CharField(
        verbose_name="Where on the right hand is the extra digit located?",
        max_length=1,
        choices=(('1', 'Near the 5th digit (little finger, pinky finger)'),
                 ('2', 'Near the thumb'), ('3', 'Other place')),
        help_text="", )

    extradigit_rhand_bone = models.CharField(
        verbose_name="Does the extra digit appear as:",
        max_length=1,
        choices=(('1',
                  'A fullly formed extra digit (seems to look like a finger and have bone in it)'),
                 ('2', 'Soft, without a bone (sometimes hanging by a stalk)')),
        help_text="", )

    extra_digit_rfoot = models.CharField(
        verbose_name="Where on the right foot is the extra digit located?",
        max_length=1,
        choices=(
        ('1', 'Near the 5th digit (little toe, pinky toe)'), ('2', 'Near the big toe'),
        ('3', 'Other place')),
        help_text="", )

    extradigit_rfoot_bone = models.CharField(
        verbose_name="Does the extra digit appear as:",
        max_length=1,
        choices=(('1',
                  'A fullly formed extra digit (seems to look like a finger and have bone in it)'),
                 ('2', 'Soft, without a bone (sometimes hanging by a stalk)')),
        help_text="", )

    extra_digit_lfoot = models.CharField(
        verbose_name="Where on the left foot is the extra digit located?",
        max_length=1,
        choices=(
        ('1', 'Near the 5th digit (little toe, pinky toe)'), ('2', 'Near the big toe'),
        ('3', 'Other place')),
        help_text="", )

    extradigit_lfoot_bone = models.CharField(
        verbose_name="Does the extra digit appear as:",
        max_length=1,
        choices=(('1',
                  'A fullly formed extra digit (seems to look like a finger and have bone in it)'),
                 ('2', 'Soft, without a bone (sometimes hanging by a stalk)')),
        help_text="", )

    headneck = models.CharField(
        verbose_name="Is the Head and neck exam NORMAL? (includes skull, fontanelles, eyes, ears, nose, jaw)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    confirm_medicalrecord = models.CharField(
        verbose_name="Did you confirm with this participant that ALL of the following information is correct in her medical record:1. HIV status2. ART regimen3. ART start date4. HIV diagnosis date5. Any history of Seizures or Epilepsy6. On any seizure or epilepsy medications at the time of conception?7. History of Diabetes BEFORE pregnancy? (only chronic diabetes, not diabetes that comes during pregnancy and then goes away after delivery)8. On any Insulin for diabetes at the time of conception?9. Type of vitamins and date prescribed?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    unable_confirmmr = models.TextField(
        verbose_name="If unable to verify the medical record for all required information, please explain:",
        help_text="", )

    handndescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    hydro = models.CharField(
        verbose_name="Is there evidence of hydrocephalus (swollen head)?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    skulldefect = models.CharField(
        verbose_name="Is there a defect in the skull?",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'No'), ('99', 'UNKNOWN')),
        help_text="", )

    skulldefect_desc = models.CharField(
        verbose_name="If there is a defect in the skull, is it:",
        max_length=2,
        choices=(('1', 'Completely covered by skin'), ('2', 'Partly covered by skin'),
                 ('3', 'Covered by a thin sac/membrane'),
                 ('4', 'Not covered by skin (brain tissue visible)'), ('99', 'UNKNOWN')),
        help_text="", )

    mouth = models.CharField(
        verbose_name="Is the mouth, lip and palate exam NORMAL? (? cleft lip or palate)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    mouthdescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    chest = models.CharField(
        verbose_name="Is the chest exam NORMAL? (? shape and respiratory movements)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    chestdescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    abdomen = models.CharField(
        verbose_name="Are the Abdominal and Anal exam NORMAL? (?masses/anal closure defect)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    abddescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    arms = models.CharField(
        verbose_name="Are the Arms and Legs NORMAL? (?length, ?shape, ?missing parts)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    armsdescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    fingers = models.CharField(
        verbose_name="Are the fingers and toes NORMAL? (including nails, ?number, dangling fused, shape or parts missing, abnormally large or small)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    fingerdescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    spine = models.CharField(
        verbose_name="Is the Spine exam NORMAL? (?lumps or ?cysts or buldging n the back including the neck, thorax or lumbar area)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    spinedescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    spdefectloc = models.CharField(
        verbose_name="Where in the spine is the defect located?",
        max_length=1,
        choices=(
        ('1', 'Cervical'), ('2', 'Thoracic'), ('3', 'Lumbosacral'), ('4', 'UNKNOWN')),
        help_text="Check All that Apply", )

    spine_defectdesc = models.CharField(
        verbose_name="Is the spinal defect:",
        max_length=2,
        choices=(('1', 'Covered in hair and NOT bulging out'),
                 ('2', 'Covered in hair and bulging out'),
                 ('3', 'Bulging out and completely covered with skin'),
                 ('4', 'Bulging out and partly covered with skin'),
                 ('5', 'Bulging out and covered with only a sac/thin membrane'),
                 ('6', 'Open-can see the spine/spinal cord'), ('99', 'UNKNOWN')),
        help_text="", )

    hips = models.CharField(
        verbose_name="Are the hips and genitalia NORMAL? (including urethra, testes, penile shaft, vagina, labia)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    hipsdescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    skin = models.CharField(
        verbose_name="Is the Skin exam NORMAL? (?pale, blue, birth marks, or any large very red areas)",
        max_length=2,
        choices=(('1', 'Yes'), ('0', 'NO'), ('99', 'UNKNOWN')),
        help_text="", )

    skindescribe = models.TextField(
        verbose_name="Description of Abnormality: (please include as much detail as possible)",
        help_text="", )

    otherca = models.TextField(
        verbose_name="Describe any other abnormality, unusual finding or make any comment about abnormality:",
        blank=True, null=True,
        help_text="", )

    modocument = models.CharField(
        verbose_name="Did a medical officer or physician document a diagnosis?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    moddx = models.TextField(
        verbose_name="Specify MO/Physician Diagnosis (or diagnoses)",
        help_text="", )

    holmesreview = models.CharField(
        verbose_name="Congenital Abnormality reviewed by Dr. Holmes?**TO BE FILLED OUT BY DR. HOLMES ONLY**",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        help_text="", )

    caddx = models.TextField(
        verbose_name="Final Diagnosis by Dr. Holmes**TO BE FILLED OUT BY DR. HOLMES ONLY**",
        help_text="", )

    certain_ca = models.CharField(
        verbose_name="How certain is this diagnosis?",
        max_length=1,
        choices=(
        ('1', 'Definite'), ('2', 'Probable'), ('3', 'Possible'), ('4', 'Uncertain')),
        blank=True, null=True,
        help_text="", )

    ca_list = models.CharField(
        verbose_name="What is the abnormality?(check all that apply)",
        max_length=3,
        choices=(('50', '45x (possible)'), ('4', 'abdominal distention'),
                 ('51', 'absence of hand'), ('52', 'absense of forearm'),
                 ('1', 'absent radius'), ('53', 'adactaly'), ('2', 'albino'),
                 ('39', 'ambiguous genitalia'), ('49', 'amniotic band syndrome'),
                 ('3', 'anencephaly'), ('54', 'anencephaly with craniorachischisis'),
                 ('37', 'ankyloglossia'), ('55', 'anopthalmia'),
                 ('56', 'arthrogryphosis'), ('57', 'asymmetric face'),
                 ('58', 'benign cyst at urethral opening'), ('48', 'bifid thumb'),
                 ('170', 'bifid toe'), ('5', 'birth injury'), ('59', 'birthmark'),
                 ('47', 'black/blue nevi'),
                 ('43', 'calcaneovalgus deformity, bilateral feet'),
                 ('60', 'calcaneovalgus deformity, unilateral foot'), ('61', 'caput'),
                 ('62', 'cardiac defect'), ('46', 'cebocephaly'),
                 ('63', 'chest wall defect'), ('64', 'chordae'),
                 ('65', 'chromosomal abnormality'), ('66', 'cleft hand'),
                 ('6', 'cleft lip'), ('7', 'cleft palate'), ('67', 'congenital cataract'),
                 ('68', 'congential absence/reduction of tibia'),
                 ('69', 'connective tissue disorder'), ('70', 'craniofacial anomolies'),
                 ('8', 'crypthopathmos'), ('71', 'CT head findings of large cyst'),
                 ('72', 'cup ear deformity'), ('45', 'cystic hygroma'),
                 ('73', 'decreased muscle tone (legs)'), ('9', 'dental cyst'),
                 ('75', 'depressed nasal ridge'),
                 ('76', 'depression of scalp (potential birth injury)'),
                 ('40', 'disseminated hairy nevus'), ('10', 'Downs syndrome'),
                 ('77', 'duplicate nipple'), ('78', 'duplicated ear canal'),
                 ('11', 'dysmorphic facial features'), ('79', 'ear deformity'),
                 ('12', 'encephalocele'), ('80', 'enlarged labia'),
                 ('81', 'enlarged liver'), ('82', 'epidermolysis bullosa (not CA)'),
                 ('174', 'eye swelling'), ('83', 'facial abnormality'),
                 ('171', 'fetal alcohol syndrome'),
                 ('84', 'finger contractures (likely not abnormality)'),
                 ('13', 'foreskin defect'), ('85', 'gangrenous forearm'),
                 ('86', 'gastroschesis'), ('87', 'genetic syndrome'), ('88',
                                                                       'gigantism of fingers (first and second, possibly thumb), bilateral'),
                 ('16', 'glanular hypospadius'), ('89', 'growth on tongue'),
                 ('90', 'gynecomastia'), ('91', 'hand deformity (unspecified)'),
                 ('92', 'hemangiomas'), ('93', 'hematoma'), ('94', 'holoprosencephaly'),
                 ('95', 'hydrocele'), ('14', 'hydrocephalus'), ('96', 'hydronephrosis'),
                 ('15', 'hyperextended leg'), ('97', 'hyperpigmentation'),
                 ('98', 'hypodactaly'), ('99', 'hypopigmented patches'),
                 ('100', 'hypospadias, NOS'), ('18', 'imperforate anus'),
                 ('101', 'increased space between first and second toe'),
                 ('102', 'inguinal hernia'), ('103', 'iniencephaly'),
                 ('19', 'isolated bowed tibia'), ('104', 'jaw assymetry'),
                 ('105', 'limb defect (skeletal defect vs. bilateral short femur)'),
                 ('20', 'limb-body wall defect'),
                 ('106', 'lipoma (fatty lump near spine)'), ('107', 'low set ears'), (
                 '108',
                 'major foot deformity (terminal transverse defect with loss of forefoot)'),
                 ('109', 'major limb defect'), ('110', 'malformation of umbilial vein'),
                 ('111', 'malformation of upper extremities'),
                 ('22', 'meningocele/myelomeningocele'), ('112', 'microcephaly'),
                 ('113', 'micrognathia'), ('114', 'micropthalmia'), ('115', 'microsomia'),
                 ('116', 'microtia'), ('117', 'mid-face deformity'),
                 ('118', 'monodactyly (both arms)'), ('119', 'moulding'),
                 ('21', 'multiple abnormalities of unknown etiology'),
                 ('120', 'multiple nevi (i.e. melanocytic nevi)'),
                 ('23', 'natal teeth/tooth'), ('121', 'nevocellular nevus'),
                 ('122', 'nevus'), ('24', 'omphalmocele'),
                 ('123', 'outer ear abnormality'), ('124', 'overlapping toes'),
                 ('125', 'penile deformity (bent penis)'), ('17', 'penile hypospadius'),
                 ('42', 'perineal hypospadius'), ('41', 'phimosis'),
                 ('126', 'phocomelia (shortened right arm)'),
                 ('127', 'pierre robin sequence, possible'),
                 ('128', 'positional deformity'),
                 ('129', 'postaxial polydactaly (unknown type)'),
                 ('130', 'postaxial polydactaly type A, bilateral foot'),
                 ('131', 'postaxial polydactaly type A, bilateral hand'),
                 ('132', 'postaxial polydactaly type A, unilateral foot'),
                 ('133', 'postaxial polydactaly type A, unilateral hand'),
                 ('134', 'postaxial polydactaly type B (bilateral) foot'),
                 ('26', 'postaxial polydactaly type B (bilateral) hand'),
                 ('25', 'postaxial polydactaly type B (unilateral) hand'),
                 ('27', 'postaxial polydactaly type B (unilaterall) foot'),
                 ('28', 'pre-auricular skin tag'),
                 ('32', 'preaxial polydactaly bilateral foot'),
                 ('30', 'preaxial polydactaly bilateral hand'),
                 ('31', 'preaxial polydactaly unilateral foot'),
                 ('29', 'preaxial polydactaly unilateral hand'), (
                 '135', 'protruding left eye in macerated stillbirth or protruding eyes'),
                 ('136', 'prune belly syndrome'),
                 ('137', 'right sided facial palsy (6th cranial nerve)'), ('138',
                                                                           'ruggae on skin of skull (underlying abnormality of skull/brain)'),
                 ('139', 'sacrococcygeal teratoma'), ('140', 'scalp defect'),
                 ('141', 'sebaceous nevus'), ('142',
                                              'short nasal bone with anteverted nostrils and absence of filtrum, could be fetal alcohol syndrome.'),
                 ('34', 'skeletal dysplasia'), ('172', 'skin tag'),
                 ('143', 'small growth near breast'), ('144', 'small nose'),
                 ('145', 'small penis'), ('146', 'spinal abnromalities'),
                 ('147', 'split foot/split hand deformity'),
                 ('148', 'swelling of right face and chest'), ('173', 'swollen labia'),
                 ('149', 'syndactaly'), ('150', 'syndactaly of toes'),
                 ('151', 'syndactly of toes with gigantism'), ('152', 'talipes'),
                 ('36', 'talipes equinovarus bilateral'),
                 ('35', 'talipes equinovarus unilateral'), ('153', 'tetrafocal melia'),
                 ('154', 'thumb hypoplasia'),
                 ('155', 'total absence of chest and abdominal wall'),
                 ('156', 'tragus deformity'), ('157', 'triphalyngeal thumb'),
                 ('158', 'trisomy 13'), ('159', 'trisomy 18'), ('160', 'trisomy 21'),
                 ('161', 'twisted umbilical cord'), ('38', 'umbilical hernia'),
                 ('162', 'underdevelopment of the lower face'),
                 ('163', 'undescended testicles'), ('164', 'unilateral cleft lip'),
                 ('0', 'unknown'), ('165', 'vaginal fistula'), ('166', 'vaginal polyp'),
                 ('44', 'vaginal tag'), ('167', 'vascular malformation'),
                 ('168', 'vascular malformation (severe)'), ('169', 'wide fontanelle'),
                 ('175', 'Absence of Tibia'), ('176', 'Brachial cleft cyst'),
                 ('177', 'Central digit hypoplasia'), ('178', 'Chest asymmetry'),
                 ('179', 'Dextrocardia'),
                 ('180', 'Deformed/abnormal upper extremity (no further description)'),
                 ('181', 'Deformed lower extremity (no further description)'),
                 ('182', 'Deformed head (no further description)'),
                 ('205', 'Deformed face/Facial abnormalities (no further description)'),
                 ('202', 'Esophageal fistula'), ('203', 'Epispadias'),
                 ('183', 'Excess hair'), ('184', 'Fetal hydrops (hydrops fetalis)'),
                 ('185', 'Growth on cheek'), ('186', 'Growth on tongue'),
                 ('218', 'growth on the leg'), ('211', 'hepatomegaly'),
                 ('187', 'Legs not same length'),
                 ('217', 'Large head (no hydrocephalus)'),
                 ('207', 'Multiple abnormalities (no further description)'),
                 ('213', 'No motor control in hands (drooping hands)'),
                 ('216', 'occipital cyst'), ('212', 'palpable mass in abdomen'),
                 ('188', 'Pedicle at the edge of nostril'), ('206', 'Peeling skin'),
                 ('189', 'Prominent rib'), ('190', 'Rash'), ('191', 'Renal cyst'),
                 ('192', 'Saddle scrotum'), ('215', 'short lower limbs'),
                 ('193', 'Short neck'), ('210', 'Skin lesion near armpit'),
                 ('194', 'Skin pedicle on anus'), ('195', 'Skin tag on chin'),
                 ('208', 'Small growth on the anal orifice'),
                 ('196', 'Sores on the hard palate'), ('209', 'Sore on the penis'),
                 ('204', 'Strabismus'), ('214', 'Swollen foreskin'),
                 ('197', 'Swelling of neck'),
                 ('198', 'Terminal transverse limb defect with nubbins'),
                 ('199', 'Umbilical cord abnormality'), ('200', 'Wide spaced nipples'),
                 ('201', 'Wrinkly skin'), (
                 '254', 'Absence of bladder seen on ultrasound (no visible abnormality)'),
                 ('219', 'Absence of mandible'), ('220', 'Amelia'),
                 ('221', 'adactylyia (nubbins)'), ('222', 'Absent Ulna'),
                 ('223', "Apert's syndrome"), ('224', 'Brachydactyly'),
                 ('225', 'Chest wall mass'), ('252', 'Cleft lip microform'),
                 ('226', 'Dilated bowel loops'),
                 ('227', 'elevated skin lesion of unknown etiology'),
                 ('228', 'Esophageal Atresia'), ('229', 'Enlarged testicles'),
                 ('230', 'Finger gigantism unilateral'),
                 ('231', 'foreskin discoloration'), ('232', 'Gigantism of arm'),
                 ('233', 'Gum cleft'), ('234', 'Hyperextended arms'),
                 ('253', 'Hypoplastic toes'),
                 ('235', 'incomplete formation of skull bones'), ('236', 'Large Tongue'),
                 ('237', 'Lipomyelomeningocele'), ('238', 'Lower extremity edema'),
                 ('239', 'Mass on the side of head'), ('240', 'Nasal polyp'),
                 ('241', 'Nose hypoplasia'), ('242', 'Pectus excavatum'),
                 ('243', 'Polysyndactyly'), ('244', 'Sacral dimple'),
                 ('245', 'scoliosis'), ('246', 'short 3rd toe bilaterally'),
                 ('247', 'Sirenomelia'), ('248', 'Spinal Dysraphism'),
                 ('249', 'Symbrachydactyly with overgrowth (giantism) of index finger'),
                 ('250', 'Toe Gigantism'),
                 ('251', 'Two heads with one orbit and two eyeballs'),
                 ('272', 'abdominal wall defect NOS'),
                 ('255', 'absence of nailbed on one finger'),
                 ('256', 'congenital blindness'),
                 ('257', 'extra digit, no bone, with stalk in middle of unilateral foot'),
                 ('258', 'finger hypoplasia'), ('259', 'gigantism of the leg'),
                 ('260', 'hip dysplasia'), ('261', 'lipoma of arm'),
                 ('262', 'major abnormality of the mouth'),
                 ('263', 'major foot abnormality'), ('273', 'otocephaly'),
                 ('264', 'overlapped sutures with underlying brain defect'),
                 ('274', 'potential structural defect of perineum'),
                 ('265', 'skull abnormality'),
                 ('266', 'small growth between the buttocks'),
                 ('267', 'spin bifida occulta'), ('268', 'spinal appendage'),
                 ('269', 'sublingual cyst'), ('270', 'turned out toe'),
                 ('271', 'unusual birth condition, possible ectopic pregnancy')),
        help_text="", )

    ca_list_twin = models.CharField(
        verbose_name="What is the abnormality in the TWIN (or second birth if triplets)?(check all that apply)",
        max_length=3,
        choices=(('50', '45x (possible)'), ('4', 'abdominal distention'),
                 ('51', 'absence of hand'), ('52', 'absense of forearm'),
                 ('1', 'absent radius'), ('53', 'adactaly'), ('2', 'albino'),
                 ('39', 'ambiguous genitalia'), ('49', 'amniotic band syndrome'),
                 ('3', 'anencephaly'), ('54', 'anencephaly with craniorachischisis'),
                 ('37', 'ankyloglossia'), ('55', 'anopthalmia'),
                 ('56', 'arthrogryphosis'), ('57', 'asymmetric face'),
                 ('58', 'benign cyst at urethral opening'), ('48', 'bifid thumb'),
                 ('170', 'bifid toe'), ('5', 'birth injury'), ('59', 'birthmark'),
                 ('47', 'black/blue nevi'),
                 ('43', 'calcaneovalgus deformity, bilateral feet'),
                 ('60', 'calcaneovalgus deformity, unilateral foot'), ('61', 'caput'),
                 ('62', 'cardiac defect'), ('46', 'cebocephaly'),
                 ('63', 'chest wall defect'), ('64', 'chordae'),
                 ('65', 'chromosomal abnormality'), ('66', 'cleft hand'),
                 ('6', 'cleft lip'), ('7', 'cleft palate'), ('67', 'congenital cataract'),
                 ('68', 'congential absence/reduction of tibia'),
                 ('69', 'connective tissue disorder'), ('70', 'craniofacial anomolies'),
                 ('8', 'crypthopathmos'), ('71', 'CT head findings of large cyst'),
                 ('72', 'cup ear deformity'), ('45', 'cystic hygroma'),
                 ('73', 'decreased muscle tone (legs)'), ('9', 'dental cyst'),
                 ('75', 'depressed nasal ridge'),
                 ('76', 'depression of scalp (potential birth injury)'),
                 ('40', 'disseminated hairy nevus'), ('10', 'Downs syndrome'),
                 ('77', 'duplicate nipple'), ('78', 'duplicated ear canal'),
                 ('11', 'dysmorphic facial features'), ('79', 'ear deformity'),
                 ('12', 'encephalocele'), ('80', 'enlarged labia'),
                 ('81', 'enlarged liver'), ('82', 'epidermolysis bullosa (not CA)'),
                 ('174', 'eye swelling'), ('83', 'facial abnormality'),
                 ('171', 'fetal alcohol syndrome'),
                 ('84', 'finger contractures (likely not abnormality)'),
                 ('13', 'foreskin defect'), ('85', 'gangrenous forearm'),
                 ('86', 'gastroschesis'), ('87', 'genetic syndrome'),
                 ('88', 'gigantism of fingers (first and second, possibly thumb), '
                        'bilateral'),
                 ('16', 'glanular hypospadius'), ('89', 'growth on tongue'),
                 ('90', 'gynecomastia'), ('91', 'hand deformity (unspecified)'),
                 ('92', 'hemangiomas'), ('93', 'hematoma'), ('94', 'holoprosencephaly'),
                 ('95', 'hydrocele'), ('14', 'hydrocephalus'), ('96', 'hydronephrosis'),
                 ('15', 'hyperextended leg'), ('97', 'hyperpigmentation'),
                 ('98', 'hypodactaly'), ('99', 'hypopigmented patches'),
                 ('100', 'hypospadias, NOS'), ('18', 'imperforate anus'),
                 ('101', 'increased space between first and second toe'),
                 ('102', 'inguinal hernia'), ('103', 'iniencephaly'),
                 ('19', 'isolated bowed tibia'), ('104', 'jaw assymetry'),
                 ('105', 'limb defect (skeletal defect vs. bilateral short femur)'),
                 ('20', 'limb-body wall defect'),
                 ('106', 'lipoma (fatty lump near spine)'), ('107', 'low set ears'), (
                 '108',
                 'major foot deformity (terminal transverse defect with loss of forefoot)'),
                 ('109', 'major limb defect'), ('110', 'malformation of umbilial vein'),
                 ('111', 'malformation of upper extremities'),
                 ('22', 'meningocele/myelomeningocele'), ('112', 'microcephaly'),
                 ('113', 'micrognathia'), ('114', 'micropthalmia'), ('115', 'microsomia'),
                 ('116', 'microtia'), ('117', 'mid-face deformity'),
                 ('118', 'monodactyly (both arms)'), ('119', 'moulding'),
                 ('21', 'multiple abnormalities of unknown etiology'),
                 ('120', 'multiple nevi (i.e. melanocytic nevi)'),
                 ('23', 'natal teeth/tooth'), ('121', 'nevocellular nevus'),
                 ('122', 'nevus'), ('24', 'omphalmocele'),
                 ('123', 'outer ear abnormality'), ('124', 'overlapping toes'),
                 ('125', 'penile deformity (bent penis)'), ('17', 'penile hypospadius'),
                 ('42', 'perineal hypospadius'), ('41', 'phimosis'),
                 ('126', 'phocomelia (shortened right arm)'),
                 ('127', 'pierre robin sequence, possible'),
                 ('128', 'positional deformity'),
                 ('129', 'postaxial polydactaly (unknown type)'),
                 ('130', 'postaxial polydactaly type A, bilateral foot'),
                 ('131', 'postaxial polydactaly type A, bilateral hand'),
                 ('132', 'postaxial polydactaly type A, unilateral foot'),
                 ('133', 'postaxial polydactaly type A, unilateral hand'),
                 ('134', 'postaxial polydactaly type B (bilateral) foot'),
                 ('26', 'postaxial polydactaly type B (bilateral) hand'),
                 ('25', 'postaxial polydactaly type B (unilateral) hand'),
                 ('27', 'postaxial polydactaly type B (unilaterall) foot'),
                 ('28', 'pre-auricular skin tag'),
                 ('32', 'preaxial polydactaly bilateral foot'),
                 ('30', 'preaxial polydactaly bilateral hand'),
                 ('31', 'preaxial polydactaly unilateral foot'),
                 ('29', 'preaxial polydactaly unilateral hand'), (
                 '135', 'protruding left eye in macerated stillbirth or protruding eyes'),
                 ('136', 'prune belly syndrome'),
                 ('137', 'right sided facial palsy (6th cranial nerve)'), ('138',
                                                                           'ruggae on skin of skull (underlying abnormality of skull/brain)'),
                 ('139', 'sacrococcygeal teratoma'), ('140', 'scalp defect'),
                 ('141', 'sebaceous nevus'), ('142',
                                              'short nasal bone with anteverted nostrils and absence of filtrum, could be fetal alcohol syndrome.'),
                 ('34', 'skeletal dysplasia'), ('172', 'skin tag'),
                 ('143', 'small growth near breast'), ('144', 'small nose'),
                 ('145', 'small penis'), ('146', 'spinal abnromalities'),
                 ('147', 'split foot/split hand deformity'),
                 ('148', 'swelling of right face and chest'), ('173', 'swollen labia'),
                 ('149', 'syndactaly'), ('150', 'syndactaly of toes'),
                 ('151', 'syndactly of toes with gigantism'), ('152', 'talipes'),
                 ('36', 'talipes equinovarus bilateral'),
                 ('35', 'talipes equinovarus unilateral'), ('153', 'tetrafocal melia'),
                 ('154', 'thumb hypoplasia'),
                 ('155', 'total absence of chest and abdominal wall'),
                 ('156', 'tragus deformity'), ('157', 'triphalyngeal thumb'),
                 ('158', 'trisomy 13'), ('159', 'trisomy 18'), ('160', 'trisomy 21'),
                 ('161', 'twisted umbilical cord'), ('38', 'umbilical hernia'),
                 ('162', 'underdevelopment of the lower face'),
                 ('163', 'undescended testicles'), ('164', 'unilateral cleft lip'),
                 ('0', 'unknown'), ('165', 'vaginal fistula'), ('166', 'vaginal polyp'),
                 ('44', 'vaginal tag'), ('167', 'vascular malformation'),
                 ('168', 'vascular malformation (severe)'), ('169', 'wide fontanelle'),
                 ('175', 'Absence of Tibia'), ('176', 'Brachial cleft cyst'),
                 ('177', 'Central digit hypoplasia'), ('178', 'Chest asymmetry'),
                 ('179', 'Dextrocardia'),
                 ('180', 'Deformed/abnormal upper extremity (no further description)'),
                 ('181', 'Deformed lower extremity (no further description)'),
                 ('182', 'Deformed head (no further description)'),
                 ('205', 'Deformed face/Facial abnormalities (no further description)'),
                 ('202', 'Esophageal fistula'), ('203', 'Epispadias'),
                 ('183', 'Excess hair'), ('184', 'Fetal hydrops (hydrops fetalis)'),
                 ('185', 'Growth on cheek'), ('186', 'Growth on tongue'),
                 ('218', 'growth on the leg'), ('211', 'hepatomegaly'),
                 ('187', 'Legs not same length'),
                 ('217', 'Large head (no hydrocephalus)'),
                 ('207', 'Multiple abnormalities (no further description)'),
                 ('213', 'No motor control in hands (drooping hands)'),
                 ('216', 'occipital cyst'), ('212', 'palpable mass in abdomen'),
                 ('188', 'Pedicle at the edge of nostril'), ('206', 'Peeling skin'),
                 ('189', 'Prominent rib'), ('190', 'Rash'), ('191', 'Renal cyst'),
                 ('192', 'Saddle scrotum'), ('215', 'short lower limbs'),
                 ('193', 'Short neck'), ('210', 'Skin lesion near armpit'),
                 ('194', 'Skin pedicle on anus'), ('195', 'Skin tag on chin'),
                 ('208', 'Small growth on the anal orifice'),
                 ('196', 'Sores on the hard palate'), ('209', 'Sore on the penis'),
                 ('204', 'Strabismus'), ('214', 'Swollen foreskin'),
                 ('197', 'Swelling of neck'),
                 ('198', 'Terminal transverse limb defect with nubbins'),
                 ('199', 'Umbilical cord abnormality'), ('200', 'Wide spaced nipples'),
                 ('201', 'Wrinkly skin'), (
                 '254', 'Absence of bladder seen on ultrasound (no visible abnormality)'),
                 ('219', 'Absence of mandible'), ('220', 'Amelia'),
                 ('221', 'adactylyia (nubbins)'), ('222', 'Absent Ulna'),
                 ('223', "Apert's syndrome"), ('224', 'Brachydactyly'),
                 ('225', 'Chest wall mass'), ('252', 'Cleft lip microform'),
                 ('226', 'Dilated bowel loops'),
                 ('227', 'elevated skin lesion of unknown etiology'),
                 ('228', 'Esophageal Atresia'), ('229', 'Enlarged testicles'),
                 ('230', 'Finger gigantism unilateral'),
                 ('231', 'foreskin discoloration'), ('232', 'Gigantism of arm'),
                 ('233', 'Gum cleft'), ('234', 'Hyperextended arms'),
                 ('253', 'Hypoplastic toes'),
                 ('235', 'incomplete formation of skull bones'), ('236', 'Large Tongue'),
                 ('237', 'Lipomyelomeningocele'), ('238', 'Lower extremity edema'),
                 ('239', 'Mass on the side of head'), ('240', 'Nasal polyp'),
                 ('241', 'Nose hypoplasia'), ('242', 'Pectus excavatum'),
                 ('243', 'Polysyndactyly'), ('244', 'Sacral dimple'),
                 ('245', 'scoliosis'), ('246', 'short 3rd toe bilaterally'),
                 ('247', 'Sirenomelia'), ('248', 'Spinal Dysraphism'),
                 ('249', 'Symbrachydactyly with overgrowth (giantism) of index finger'),
                 ('250', 'Toe Gigantism'),
                 ('251', 'Two heads with one orbit and two eyeballs'),
                 ('272', 'abdominal wall defect NOS'),
                 ('255', 'absence of nailbed on one finger'),
                 ('256', 'congenital blindness'),
                 ('257', 'extra digit, no bone, with stalk in middle of unilateral foot'),
                 ('258', 'finger hypoplasia'), ('259', 'gigantism of the leg'),
                 ('260', 'hip dysplasia'), ('261', 'lipoma of arm'),
                 ('262', 'major abnormality of the mouth'),
                 ('263', 'major foot abnormality'), ('273', 'otocephaly'),
                 ('264', 'overlapped sutures with underlying brain defect'),
                 ('274', 'potential structural defect of perineum'),
                 ('265', 'skull abnormality'),
                 ('266', 'small growth between the buttocks'),
                 ('267', 'spin bifida occulta'), ('268', 'spinal appendage'),
                 ('269', 'sublingual cyst'), ('270', 'turned out toe'),
                 ('271', 'unusual birth condition, possible ectopic pregnancy')),
        help_text="", )

    ca_list_triplet = models.CharField(
        verbose_name="What is the abnormality in the TRIPLET (or third birth if quadruplets)?(check all that apply)",
        max_length=3,
        choices=(('50', '45x (possible)'), ('4', 'abdominal distention'),
                 ('51', 'absence of hand'), ('52', 'absense of forearm'),
                 ('1', 'absent radius'), ('53', 'adactaly'), ('2', 'albino'),
                 ('39', 'ambiguous genitalia'), ('49', 'amniotic band syndrome'),
                 ('3', 'anencephaly'), ('54', 'anencephaly with craniorachischisis'),
                 ('37', 'ankyloglossia'), ('55', 'anopthalmia'),
                 ('56', 'arthrogryphosis'), ('57', 'asymmetric face'),
                 ('58', 'benign cyst at urethral opening'), ('48', 'bifid thumb'),
                 ('170', 'bifid toe'), ('5', 'birth injury'), ('59', 'birthmark'),
                 ('47', 'black/blue nevi'),
                 ('43', 'calcaneovalgus deformity, bilateral feet'),
                 ('60', 'calcaneovalgus deformity, unilateral foot'), ('61', 'caput'),
                 ('62', 'cardiac defect'), ('46', 'cebocephaly'),
                 ('63', 'chest wall defect'), ('64', 'chordae'),
                 ('65', 'chromosomal abnormality'), ('66', 'cleft hand'),
                 ('6', 'cleft lip'), ('7', 'cleft palate'), ('67', 'congenital cataract'),
                 ('68', 'congential absence/reduction of tibia'),
                 ('69', 'connective tissue disorder'), ('70', 'craniofacial anomolies'),
                 ('8', 'crypthopathmos'), ('71', 'CT head findings of large cyst'),
                 ('72', 'cup ear deformity'), ('45', 'cystic hygroma'),
                 ('73', 'decreased muscle tone (legs)'), ('9', 'dental cyst'),
                 ('75', 'depressed nasal ridge'),
                 ('76', 'depression of scalp (potential birth injury)'),
                 ('40', 'disseminated hairy nevus'), ('10', 'Downs syndrome'),
                 ('77', 'duplicate nipple'), ('78', 'duplicated ear canal'),
                 ('11', 'dysmorphic facial features'), ('79', 'ear deformity'),
                 ('12', 'encephalocele'), ('80', 'enlarged labia'),
                 ('81', 'enlarged liver'), ('82', 'epidermolysis bullosa (not CA)'),
                 ('174', 'eye swelling'), ('83', 'facial abnormality'),
                 ('171', 'fetal alcohol syndrome'),
                 ('84', 'finger contractures (likely not abnormality)'),
                 ('13', 'foreskin defect'), ('85', 'gangrenous forearm'),
                 ('86', 'gastroschesis'), ('87', 'genetic syndrome'), ('88',
                                                                       'gigantism of fingers (first and second, possibly thumb), bilateral'),
                 ('16', 'glanular hypospadius'), ('89', 'growth on tongue'),
                 ('90', 'gynecomastia'), ('91', 'hand deformity (unspecified)'),
                 ('92', 'hemangiomas'), ('93', 'hematoma'), ('94', 'holoprosencephaly'),
                 ('95', 'hydrocele'), ('14', 'hydrocephalus'), ('96', 'hydronephrosis'),
                 ('15', 'hyperextended leg'), ('97', 'hyperpigmentation'),
                 ('98', 'hypodactaly'), ('99', 'hypopigmented patches'),
                 ('100', 'hypospadias, NOS'), ('18', 'imperforate anus'),
                 ('101', 'increased space between first and second toe'),
                 ('102', 'inguinal hernia'), ('103', 'iniencephaly'),
                 ('19', 'isolated bowed tibia'), ('104', 'jaw assymetry'),
                 ('105', 'limb defect (skeletal defect vs. bilateral short femur)'),
                 ('20', 'limb-body wall defect'),
                 ('106', 'lipoma (fatty lump near spine)'), ('107', 'low set ears'), (
                 '108',
                 'major foot deformity (terminal transverse defect with loss of forefoot)'),
                 ('109', 'major limb defect'), ('110', 'malformation of umbilial vein'),
                 ('111', 'malformation of upper extremities'),
                 ('22', 'meningocele/myelomeningocele'), ('112', 'microcephaly'),
                 ('113', 'micrognathia'), ('114', 'micropthalmia'), ('115', 'microsomia'),
                 ('116', 'microtia'), ('117', 'mid-face deformity'),
                 ('118', 'monodactyly (both arms)'), ('119', 'moulding'),
                 ('21', 'multiple abnormalities of unknown etiology'),
                 ('120', 'multiple nevi (i.e. melanocytic nevi)'),
                 ('23', 'natal teeth/tooth'), ('121', 'nevocellular nevus'),
                 ('122', 'nevus'), ('24', 'omphalmocele'),
                 ('123', 'outer ear abnormality'), ('124', 'overlapping toes'),
                 ('125', 'penile deformity (bent penis)'), ('17', 'penile hypospadius'),
                 ('42', 'perineal hypospadius'), ('41', 'phimosis'),
                 ('126', 'phocomelia (shortened right arm)'),
                 ('127', 'pierre robin sequence, possible'),
                 ('128', 'positional deformity'),
                 ('129', 'postaxial polydactaly (unknown type)'),
                 ('130', 'postaxial polydactaly type A, bilateral foot'),
                 ('131', 'postaxial polydactaly type A, bilateral hand'),
                 ('132', 'postaxial polydactaly type A, unilateral foot'),
                 ('133', 'postaxial polydactaly type A, unilateral hand'),
                 ('134', 'postaxial polydactaly type B (bilateral) foot'),
                 ('26', 'postaxial polydactaly type B (bilateral) hand'),
                 ('25', 'postaxial polydactaly type B (unilateral) hand'),
                 ('27', 'postaxial polydactaly type B (unilaterall) foot'),
                 ('28', 'pre-auricular skin tag'),
                 ('32', 'preaxial polydactaly bilateral foot'),
                 ('30', 'preaxial polydactaly bilateral hand'),
                 ('31', 'preaxial polydactaly unilateral foot'),
                 ('29', 'preaxial polydactaly unilateral hand'), (
                 '135', 'protruding left eye in macerated stillbirth or protruding eyes'),
                 ('136', 'prune belly syndrome'),
                 ('137', 'right sided facial palsy (6th cranial nerve)'), ('138',
                                                                           'ruggae on skin of skull (underlying abnormality of skull/brain)'),
                 ('139', 'sacrococcygeal teratoma'), ('140', 'scalp defect'),
                 ('141', 'sebaceous nevus'), ('142',
                                              'short nasal bone with anteverted nostrils and absence of filtrum, could be fetal alcohol syndrome.'),
                 ('34', 'skeletal dysplasia'), ('172', 'skin tag'),
                 ('143', 'small growth near breast'), ('144', 'small nose'),
                 ('145', 'small penis'), ('146', 'spinal abnromalities'),
                 ('147', 'split foot/split hand deformity'),
                 ('148', 'swelling of right face and chest'), ('173', 'swollen labia'),
                 ('149', 'syndactaly'), ('150', 'syndactaly of toes'),
                 ('151', 'syndactly of toes with gigantism'), ('152', 'talipes'),
                 ('36', 'talipes equinovarus bilateral'),
                 ('35', 'talipes equinovarus unilateral'), ('153', 'tetrafocal melia'),
                 ('154', 'thumb hypoplasia'),
                 ('155', 'total absence of chest and abdominal wall'),
                 ('156', 'tragus deformity'), ('157', 'triphalyngeal thumb'),
                 ('158', 'trisomy 13'), ('159', 'trisomy 18'), ('160', 'trisomy 21'),
                 ('161', 'twisted umbilical cord'), ('38', 'umbilical hernia'),
                 ('162', 'underdevelopment of the lower face'),
                 ('163', 'undescended testicles'), ('164', 'unilateral cleft lip'),
                 ('0', 'unknown'), ('165', 'vaginal fistula'), ('166', 'vaginal polyp'),
                 ('44', 'vaginal tag'), ('167', 'vascular malformation'),
                 ('168', 'vascular malformation (severe)'), ('169', 'wide fontanelle'),
                 ('175', 'Absence of Tibia'), ('176', 'Brachial cleft cyst'),
                 ('177', 'Central digit hypoplasia'), ('178', 'Chest asymmetry'),
                 ('179', 'Dextrocardia'),
                 ('180', 'Deformed/abnormal upper extremity (no further description)'),
                 ('181', 'Deformed lower extremity (no further description)'),
                 ('182', 'Deformed head (no further description)'),
                 ('205', 'Deformed face/Facial abnormalities (no further description)'),
                 ('202', 'Esophageal fistula'), ('203', 'Epispadias'),
                 ('183', 'Excess hair'), ('184', 'Fetal hydrops (hydrops fetalis)'),
                 ('185', 'Growth on cheek'), ('186', 'Growth on tongue'),
                 ('218', 'growth on the leg'), ('211', 'hepatomegaly'),
                 ('187', 'Legs not same length'),
                 ('217', 'Large head (no hydrocephalus)'),
                 ('207', 'Multiple abnormalities (no further description)'),
                 ('213', 'No motor control in hands (drooping hands)'),
                 ('216', 'occipital cyst'), ('212', 'palpable mass in abdomen'),
                 ('188', 'Pedicle at the edge of nostril'), ('206', 'Peeling skin'),
                 ('189', 'Prominent rib'), ('190', 'Rash'), ('191', 'Renal cyst'),
                 ('192', 'Saddle scrotum'), ('215', 'short lower limbs'),
                 ('193', 'Short neck'), ('210', 'Skin lesion near armpit'),
                 ('194', 'Skin pedicle on anus'), ('195', 'Skin tag on chin'),
                 ('208', 'Small growth on the anal orifice'),
                 ('196', 'Sores on the hard palate'), ('209', 'Sore on the penis'),
                 ('204', 'Strabismus'), ('214', 'Swollen foreskin'),
                 ('197', 'Swelling of neck'),
                 ('198', 'Terminal transverse limb defect with nubbins'),
                 ('199', 'Umbilical cord abnormality'), ('200', 'Wide spaced nipples'),
                 ('201', 'Wrinkly skin'), (
                 '254', 'Absence of bladder seen on ultrasound (no visible abnormality)'),
                 ('219', 'Absence of mandible'), ('220', 'Amelia'),
                 ('221', 'adactylyia (nubbins)'), ('222', 'Absent Ulna'),
                 ('223', "Apert's syndrome"), ('224', 'Brachydactyly'),
                 ('225', 'Chest wall mass'), ('252', 'Cleft lip microform'),
                 ('226', 'Dilated bowel loops'),
                 ('227', 'elevated skin lesion of unknown etiology'),
                 ('228', 'Esophageal Atresia'), ('229', 'Enlarged testicles'),
                 ('230', 'Finger gigantism unilateral'),
                 ('231', 'foreskin discoloration'), ('232', 'Gigantism of arm'),
                 ('233', 'Gum cleft'), ('234', 'Hyperextended arms'),
                 ('253', 'Hypoplastic toes'),
                 ('235', 'incomplete formation of skull bones'), ('236', 'Large Tongue'),
                 ('237', 'Lipomyelomeningocele'), ('238', 'Lower extremity edema'),
                 ('239', 'Mass on the side of head'), ('240', 'Nasal polyp'),
                 ('241', 'Nose hypoplasia'), ('242', 'Pectus excavatum'),
                 ('243', 'Polysyndactyly'), ('244', 'Sacral dimple'),
                 ('245', 'scoliosis'), ('246', 'short 3rd toe bilaterally'),
                 ('247', 'Sirenomelia'), ('248', 'Spinal Dysraphism'),
                 ('249', 'Symbrachydactyly with overgrowth (giantism) of index finger'),
                 ('250', 'Toe Gigantism'),
                 ('251', 'Two heads with one orbit and two eyeballs'),
                 ('272', 'abdominal wall defect NOS'),
                 ('255', 'absence of nailbed on one finger'),
                 ('256', 'congenital blindness'),
                 ('257', 'extra digit, no bone, with stalk in middle of unilateral foot'),
                 ('258', 'finger hypoplasia'), ('259', 'gigantism of the leg'),
                 ('260', 'hip dysplasia'), ('261', 'lipoma of arm'),
                 ('262', 'major abnormality of the mouth'),
                 ('263', 'major foot abnormality'), ('273', 'otocephaly'),
                 ('264', 'overlapped sutures with underlying brain defect'),
                 ('274', 'potential structural defect of perineum'),
                 ('265', 'skull abnormality'),
                 ('266', 'small growth between the buttocks'),
                 ('267', 'spin bifida occulta'), ('268', 'spinal appendage'),
                 ('269', 'sublingual cyst'), ('270', 'turned out toe'),
                 ('271', 'unusual birth condition, possible ectopic pregnancy')),
        help_text="", )

    ca_list_quad = models.CharField(
        verbose_name="What is the abnormality in the QUAD (or fourth birth if quadruplets)?(check all that apply)",
        max_length=3,
        choices=(('50', '45x (possible)'), ('4', 'abdominal distention'),
                 ('51', 'absence of hand'), ('52', 'absense of forearm'),
                 ('1', 'absent radius'), ('53', 'adactaly'), ('2', 'albino'),
                 ('39', 'ambiguous genitalia'), ('49', 'amniotic band syndrome'),
                 ('3', 'anencephaly'), ('54', 'anencephaly with craniorachischisis'),
                 ('37', 'ankyloglossia'), ('55', 'anopthalmia'),
                 ('56', 'arthrogryphosis'), ('57', 'asymmetric face'),
                 ('58', 'benign cyst at urethral opening'), ('48', 'bifid thumb'),
                 ('170', 'bifid toe'), ('5', 'birth injury'), ('59', 'birthmark'),
                 ('47', 'black/blue nevi'),
                 ('43', 'calcaneovalgus deformity, bilateral feet'),
                 ('60', 'calcaneovalgus deformity, unilateral foot'), ('61', 'caput'),
                 ('62', 'cardiac defect'), ('46', 'cebocephaly'),
                 ('63', 'chest wall defect'), ('64', 'chordae'),
                 ('65', 'chromosomal abnormality'), ('66', 'cleft hand'),
                 ('6', 'cleft lip'), ('7', 'cleft palate'), ('67', 'congenital cataract'),
                 ('68', 'congential absence/reduction of tibia'),
                 ('69', 'connective tissue disorder'), ('70', 'craniofacial anomolies'),
                 ('8', 'crypthopathmos'), ('71', 'CT head findings of large cyst'),
                 ('72', 'cup ear deformity'), ('45', 'cystic hygroma'),
                 ('73', 'decreased muscle tone (legs)'), ('9', 'dental cyst'),
                 ('75', 'depressed nasal ridge'),
                 ('76', 'depression of scalp (potential birth injury)'),
                 ('40', 'disseminated hairy nevus'), ('10', 'Downs syndrome'),
                 ('77', 'duplicate nipple'), ('78', 'duplicated ear canal'),
                 ('11', 'dysmorphic facial features'), ('79', 'ear deformity'),
                 ('12', 'encephalocele'), ('80', 'enlarged labia'),
                 ('81', 'enlarged liver'), ('82', 'epidermolysis bullosa (not CA)'),
                 ('174', 'eye swelling'), ('83', 'facial abnormality'),
                 ('171', 'fetal alcohol syndrome'),
                 ('84', 'finger contractures (likely not abnormality)'),
                 ('13', 'foreskin defect'), ('85', 'gangrenous forearm'),
                 ('86', 'gastroschesis'), ('87', 'genetic syndrome'), ('88',
                                                                       'gigantism of fingers (first and second, possibly thumb), bilateral'),
                 ('16', 'glanular hypospadius'), ('89', 'growth on tongue'),
                 ('90', 'gynecomastia'), ('91', 'hand deformity (unspecified)'),
                 ('92', 'hemangiomas'), ('93', 'hematoma'), ('94', 'holoprosencephaly'),
                 ('95', 'hydrocele'), ('14', 'hydrocephalus'), ('96', 'hydronephrosis'),
                 ('15', 'hyperextended leg'), ('97', 'hyperpigmentation'),
                 ('98', 'hypodactaly'), ('99', 'hypopigmented patches'),
                 ('100', 'hypospadias, NOS'), ('18', 'imperforate anus'),
                 ('101', 'increased space between first and second toe'),
                 ('102', 'inguinal hernia'), ('103', 'iniencephaly'),
                 ('19', 'isolated bowed tibia'), ('104', 'jaw assymetry'),
                 ('105', 'limb defect (skeletal defect vs. bilateral short femur)'),
                 ('20', 'limb-body wall defect'),
                 ('106', 'lipoma (fatty lump near spine)'), ('107', 'low set ears'), (
                 '108',
                 'major foot deformity (terminal transverse defect with loss of forefoot)'),
                 ('109', 'major limb defect'), ('110', 'malformation of umbilial vein'),
                 ('111', 'malformation of upper extremities'),
                 ('22', 'meningocele/myelomeningocele'), ('112', 'microcephaly'),
                 ('113', 'micrognathia'), ('114', 'micropthalmia'), ('115', 'microsomia'),
                 ('116', 'microtia'), ('117', 'mid-face deformity'),
                 ('118', 'monodactyly (both arms)'), ('119', 'moulding'),
                 ('21', 'multiple abnormalities of unknown etiology'),
                 ('120', 'multiple nevi (i.e. melanocytic nevi)'),
                 ('23', 'natal teeth/tooth'), ('121', 'nevocellular nevus'),
                 ('122', 'nevus'), ('24', 'omphalmocele'),
                 ('123', 'outer ear abnormality'), ('124', 'overlapping toes'),
                 ('125', 'penile deformity (bent penis)'), ('17', 'penile hypospadius'),
                 ('42', 'perineal hypospadius'), ('41', 'phimosis'),
                 ('126', 'phocomelia (shortened right arm)'),
                 ('127', 'pierre robin sequence, possible'),
                 ('128', 'positional deformity'),
                 ('129', 'postaxial polydactaly (unknown type)'),
                 ('130', 'postaxial polydactaly type A, bilateral foot'),
                 ('131', 'postaxial polydactaly type A, bilateral hand'),
                 ('132', 'postaxial polydactaly type A, unilateral foot'),
                 ('133', 'postaxial polydactaly type A, unilateral hand'),
                 ('134', 'postaxial polydactaly type B (bilateral) foot'),
                 ('26', 'postaxial polydactaly type B (bilateral) hand'),
                 ('25', 'postaxial polydactaly type B (unilateral) hand'),
                 ('27', 'postaxial polydactaly type B (unilaterall) foot'),
                 ('28', 'pre-auricular skin tag'),
                 ('32', 'preaxial polydactaly bilateral foot'),
                 ('30', 'preaxial polydactaly bilateral hand'),
                 ('31', 'preaxial polydactaly unilateral foot'),
                 ('29', 'preaxial polydactaly unilateral hand'), (
                 '135', 'protruding left eye in macerated stillbirth or protruding eyes'),
                 ('136', 'prune belly syndrome'),
                 ('137', 'right sided facial palsy (6th cranial nerve)'), ('138',
                                                                           'ruggae on skin of skull (underlying abnormality of skull/brain)'),
                 ('139', 'sacrococcygeal teratoma'), ('140', 'scalp defect'),
                 ('141', 'sebaceous nevus'), ('142',
                                              'short nasal bone with anteverted nostrils and absence of filtrum, could be fetal alcohol syndrome.'),
                 ('34', 'skeletal dysplasia'), ('172', 'skin tag'),
                 ('143', 'small growth near breast'), ('144', 'small nose'),
                 ('145', 'small penis'), ('146', 'spinal abnromalities'),
                 ('147', 'split foot/split hand deformity'),
                 ('148', 'swelling of right face and chest'), ('173', 'swollen labia'),
                 ('149', 'syndactaly'), ('150', 'syndactaly of toes'),
                 ('151', 'syndactly of toes with gigantism'), ('152', 'talipes'),
                 ('36', 'talipes equinovarus bilateral'),
                 ('35', 'talipes equinovarus unilateral'), ('153', 'tetrafocal melia'),
                 ('154', 'thumb hypoplasia'),
                 ('155', 'total absence of chest and abdominal wall'),
                 ('156', 'tragus deformity'), ('157', 'triphalyngeal thumb'),
                 ('158', 'trisomy 13'), ('159', 'trisomy 18'), ('160', 'trisomy 21'),
                 ('161', 'twisted umbilical cord'), ('38', 'umbilical hernia'),
                 ('162', 'underdevelopment of the lower face'),
                 ('163', 'undescended testicles'), ('164', 'unilateral cleft lip'),
                 ('0', 'unknown'), ('165', 'vaginal fistula'), ('166', 'vaginal polyp'),
                 ('44', 'vaginal tag'), ('167', 'vascular malformation'),
                 ('168', 'vascular malformation (severe)'), ('169', 'wide fontanelle'),
                 ('175', 'Absence of Tibia'), ('176', 'Brachial cleft cyst'),
                 ('177', 'Central digit hypoplasia'), ('178', 'Chest asymmetry'),
                 ('179', 'Dextrocardia'),
                 ('180', 'Deformed/abnormal upper extremity (no further description)'),
                 ('181', 'Deformed lower extremity (no further description)'),
                 ('182', 'Deformed head (no further description)'),
                 ('205', 'Deformed face/Facial abnormalities (no further description)'),
                 ('202', 'Esophageal fistula'), ('203', 'Epispadias'),
                 ('183', 'Excess hair'), ('184', 'Fetal hydrops (hydrops fetalis)'),
                 ('185', 'Growth on cheek'), ('186', 'Growth on tongue'),
                 ('218', 'growth on the leg'), ('211', 'hepatomegaly'),
                 ('187', 'Legs not same length'),
                 ('217', 'Large head (no hydrocephalus)'),
                 ('207', 'Multiple abnormalities (no further description)'),
                 ('213', 'No motor control in hands (drooping hands)'),
                 ('216', 'occipital cyst'), ('212', 'palpable mass in abdomen'),
                 ('188', 'Pedicle at the edge of nostril'), ('206', 'Peeling skin'),
                 ('189', 'Prominent rib'), ('190', 'Rash'), ('191', 'Renal cyst'),
                 ('192', 'Saddle scrotum'), ('215', 'short lower limbs'),
                 ('193', 'Short neck'), ('210', 'Skin lesion near armpit'),
                 ('194', 'Skin pedicle on anus'), ('195', 'Skin tag on chin'),
                 ('208', 'Small growth on the anal orifice'),
                 ('196', 'Sores on the hard palate'), ('209', 'Sore on the penis'),
                 ('204', 'Strabismus'), ('214', 'Swollen foreskin'),
                 ('197', 'Swelling of neck'),
                 ('198', 'Terminal transverse limb defect with nubbins'),
                 ('199', 'Umbilical cord abnormality'), ('200', 'Wide spaced nipples'),
                 ('201', 'Wrinkly skin'), (
                 '254', 'Absence of bladder seen on ultrasound (no visible abnormality)'),
                 ('219', 'Absence of mandible'), ('220', 'Amelia'),
                 ('221', 'adactylyia (nubbins)'), ('222', 'Absent Ulna'),
                 ('223', "Apert's syndrome"), ('224', 'Brachydactyly'),
                 ('225', 'Chest wall mass'), ('252', 'Cleft lip microform'),
                 ('226', 'Dilated bowel loops'),
                 ('227', 'elevated skin lesion of unknown etiology'),
                 ('228', 'Esophageal Atresia'), ('229', 'Enlarged testicles'),
                 ('230', 'Finger gigantism unilateral'),
                 ('231', 'foreskin discoloration'), ('232', 'Gigantism of arm'),
                 ('233', 'Gum cleft'), ('234', 'Hyperextended arms'),
                 ('253', 'Hypoplastic toes'),
                 ('235', 'incomplete formation of skull bones'), ('236', 'Large Tongue'),
                 ('237', 'Lipomyelomeningocele'), ('238', 'Lower extremity edema'),
                 ('239', 'Mass on the side of head'), ('240', 'Nasal polyp'),
                 ('241', 'Nose hypoplasia'), ('242', 'Pectus excavatum'),
                 ('243', 'Polysyndactyly'), ('244', 'Sacral dimple'),
                 ('245', 'scoliosis'), ('246', 'short 3rd toe bilaterally'),
                 ('247', 'Sirenomelia'), ('248', 'Spinal Dysraphism'),
                 ('249', 'Symbrachydactyly with overgrowth (giantism) of index finger'),
                 ('250', 'Toe Gigantism'),
                 ('251', 'Two heads with one orbit and two eyeballs'),
                 ('272', 'abdominal wall defect NOS'),
                 ('255', 'absence of nailbed on one finger'),
                 ('256', 'congenital blindness'),
                 ('257', 'extra digit, no bone, with stalk in middle of unilateral foot'),
                 ('258', 'finger hypoplasia'), ('259', 'gigantism of the leg'),
                 ('260', 'hip dysplasia'), ('261', 'lipoma of arm'),
                 ('262', 'major abnormality of the mouth'),
                 ('263', 'major foot abnormality'), ('273', 'otocephaly'),
                 ('264', 'overlapped sutures with underlying brain defect'),
                 ('274', 'potential structural defect of perineum'),
                 ('265', 'skull abnormality'),
                 ('266', 'small growth between the buttocks'),
                 ('267', 'spin bifida occulta'), ('268', 'spinal appendage'),
                 ('269', 'sublingual cyst'), ('270', 'turned out toe'),
                 ('271', 'unusual birth condition, possible ectopic pregnancy')),
        help_text="", )

    ntd = models.CharField(
        verbose_name="Is this a neural tube defect",
        max_length=1,
        choices=(('1', 'Yes (photo available)'), ('2', 'Probable (no photo available)'),
                 ('0', 'No'), ('3', 'Unknown')),
        blank=True, null=True,
        help_text="", )

    ntd_twin = models.CharField(
        verbose_name="Is TWIN's (second born in multiples) defect a neural tube defect",
        max_length=1,
        choices=(('1', 'Yes (photo available)'), ('2', 'Probable (no photo available)'),
                 ('0', 'No'), ('3', 'Unknown')),
        blank=True, null=True,
        help_text="", )

    ntd_triplet = models.CharField(
        verbose_name="Is TRIPLET's (third born in multiples) defect a neural tube defect",
        max_length=1,
        choices=(('1', 'Yes (photo available)'), ('2', 'Probable (no photo available)'),
                 ('0', 'No'), ('3', 'Unknown')),
        blank=True, null=True,
        help_text="", )

    ntd_quad = models.CharField(
        verbose_name="Is QUADRUPLET's (fourth born in multiples) defect a neural tube defect",
        max_length=1,
        choices=(('1', 'Yes (photo available)'), ('2', 'Probable (no photo available)'),
                 ('0', 'No'), ('3', 'Unknown')),
        blank=True, null=True,
        help_text="", )

    ca_majorabn = models.CharField(
        verbose_name="Is this a major abnormality?",
        max_length=2,
        choices=(('1', 'Yes (photo available)'), ('2', 'Probable (no photo available)'),
                 ('0', 'No (photo available)'), ('3', 'Unlikely (no photo available)'),
                 ('99', 'Unknown'), ('4', 'Not an abnormality')),
        help_text="", )

    ca_majorabn_twin = models.CharField(
        verbose_name="Is TWIN (second born in multiples) defect a major abnormality?",
        max_length=2,
        choices=(('1', 'Yes (photo available)'), ('2', 'Probable (no photo available)'),
                 ('0', 'No (photo available)'), ('3', 'Unlikely (no photo available)'),
                 ('99', 'Unknown'), ('4', 'Not an abnormality')),
        help_text="", )

    ca_majorabn_triplet = models.CharField(
        verbose_name="Is TRIPLET (third born in multiples) defect a major abnormality?",
        max_length=2,
        choices=(('1', 'Yes (photo available)'), ('2', 'Probable (no photo available)'),
                 ('0', 'No (photo available)'), ('3', 'Unlikely (no photo available)'),
                 ('99', 'Unknown'), ('4', 'Not an abnormality')),
        help_text="", )

    ca_majorabn_quad = models.CharField(
        verbose_name="Is QUADRUPLET (fourth born in multiples) defect a major "
                     "abnormality?",
        max_length=2,
        choices=(('1', 'Yes (photo available)'), ('2', 'Probable (no photo available)'),
                 ('0', 'No (photo available)'), ('3', 'Unlikely (no photo available)'),
                 ('99', 'Unknown'), ('4', 'Not an abnormality')),
        help_text="", )

    ca_reportedmom = models.CharField(
        verbose_name="Did this mother call/return to find out Dr. Holmes diagnosis?",
        max_length=1,
        choices=(('1', 'Yes'), ('0', 'No')),
        blank=True, null=True,
        help_text="", )

    followup_ca = models.TextField(
        verbose_name="Is there any further information about the baby that was obtained when the mother called/returned for her result? (for example, baby died, or the abnormality has been surgically fixed, or the head is no longer large, etc.)",
        blank=True, null=True,
        help_text="", )

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Tsepamo 2'
        verbose_name_plural = 'Tsepamo 2'
