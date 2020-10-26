from django.contrib import admin
from django.urls import path

from .views import UserCreateRetrieveView


app_name = 'core'

urlpatterns = [
    path('user/', UserCreateRetrieveView.as_view(), name='user'),
]
