from django.contrib import admin
from django.urls import path

from .views import VideoItemsSearchResults, search_videos


app_name = 'core'

urlpatterns = [
    # path('search/', VideoItemsSearchResults.as_view(), name='search_video_item'),
    path('search/', search_videos, name='search_video_item'),
]
