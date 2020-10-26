from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    pass
