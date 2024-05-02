
from .model_mixins import (CompleteFieldMixin, UuidModelMixin, RecordIDModelMixin,
                           OutcomesModelMixin)


class OutcomesOne(UuidModelMixin, RecordIDModelMixin, OutcomesModelMixin,
                  CompleteFieldMixin):

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Outcomes 1'
        verbose_name_plural = 'Outcomes 1'
