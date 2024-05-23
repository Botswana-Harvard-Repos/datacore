from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLES = (
        ('administrator', 'Administrator'),
        ('coordinator', 'Coordinator'),
    )

    role = models.CharField(
        max_length=20,
        choices=USER_ROLES)
