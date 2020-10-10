from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class User(AbstractUser, TimeStampedModel):
    pass


class UserVideoItem(TimeStampedModel):
    MOVIE = 'movie'
    SERIES = 'series'
    CATEGORIES = [
        (MOVIE, "Movie"),
        (SERIES, "Series"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imdb_id = models.CharField(max_length=255)
    date_watched = models.DateField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORIES, default=MOVIE)

    class Meta:
        unique_together = ('user', 'imdb_id',)
