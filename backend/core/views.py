import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import UserVideoItem
from .serializers import UserSerializer, UserVideoItemSerializer


class UserVideoItemListCreateView(generics.ListCreateAPIView):
    model = UserVideoItem
    serializer_class = UserVideoItemSerializer
    queryset = UserVideoItem.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)




def search_videos(request):
    search_param = request.GET.get('s')

    response = {'results': []}
    if search_param:
        response = requests.get(f'{settings.OMDB_API_URL}s={search_param}')
        response = response.content.decode()
        response = json.loads(response)
        user = 1  # request.user
        uvis = UserVideoItem.objects.filter(user__id=user)  # TODO: continue from here - execute lazy query before getting into the for loop
        for result in response:
            record = uvis.filter(imdb_id=result['imdbID'])
            try:
                uvi = UserVideoItem.objects.filter(user__id=user, imdb_id=result['imdbID'])

            except UserVideoItem.DoesNotExist:
                pass


    return JsonResponse(response)
