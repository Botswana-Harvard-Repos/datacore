from decimal import Decimal
from bson.decimal128 import Decimal128
from django.db import models


class DecimalFieldMixin(models.Model):

    def clean_decimal_fields(self):
        for field_name, value in self.__dict__.items():
            if isinstance(value, Decimal128):
                # Convert Decimal128 fields to Decimal
                setattr(self, field_name,
                        self.convert_decimal128_to_decimal(value))
            elif isinstance(value, Decimal):
                # Ensure all decimals are of the correct type
                setattr(self, field_name, Decimal(value))

    def convert_decimal128_to_decimal(self,value):
        if isinstance(value, Decimal128):
            # Convert Decimal128 to Decimal
            return value.to_decimal()
        return value

    def save(self, *args, **kwargs):
        # Before saving, clean the decimal fields
        self.clean_decimal_fields()
        # Assuming you have some method to save the document to MongoDB
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
