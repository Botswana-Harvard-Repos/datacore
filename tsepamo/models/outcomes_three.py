
from .model_mixins import (CompleteFieldMixin, UuidModelMixin, RecordIDModelMixin,
                           OutcomesModelMixin)


class OutcomesThree(UuidModelMixin, RecordIDModelMixin, CompleteFieldMixin,
                    OutcomesModelMixin):

    class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Outcomes 3'
        verbose_name_plural = 'Outcomes 3'
