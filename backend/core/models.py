from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class User(AbstractUser, TimeStampedModel):
    pass


class UserVideoItem(TimeStampedModel):
    MOVIE = 'M'
    SERIES = 'S'
    CATEGORIES = [
        (MOVIE, "Movie"),
        (SERIES, "Series"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imdb_id = models.CharField(max_length=255)
    date_watched = models.DateField(blank=True, null=True)
    rating = models.FloatField()
    category = models.CharField(max_length=2, choices=CATEGORIES, default=MOVIE)
