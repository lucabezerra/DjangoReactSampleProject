from django.contrib import admin
from django.urls import path

from .views import UserVideoItemListCreateView, search_videos


app_name = 'videos'

urlpatterns = [
    path('search/', search_videos, name='search_video'),
    path('video/', UserVideoItemListCreateView.as_view(), name='user_video_item'),
]
