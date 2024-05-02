from django.db import models


class CompleteFieldMixin(models.Model):

    complete = models.CharField(
        verbose_name='Complete?',
        blank=True,
        null=True,
        help_text='',
        choices=(('0', 'Incomplete'),
                 ('1', 'Unverified'),
                 ('2', 'Complete')),
        max_length=1
    )

    class Meta:
        abstract = True
