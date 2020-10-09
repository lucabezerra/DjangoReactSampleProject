import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics

from .models import UserVideoItem
from .serializers import UserSerializer, UserVideoItemSerializer

# Create your views here.

class VideoItemsSearchResults(generics.ListAPIView):
    model = UserVideoItem
    serializer = UserVideoItemSerializer


def search_videos(request):
    search_param = request.GET.get('s')

    response = {'results': []}
    if search_param:
        response = requests.get(f'{settings.OMDB_API_URL}s={search_param}')
        response = response.content.decode()
        response = json.loads(response)

    return JsonResponse(response)


'''
{"Search":[{"Title":"There\'s Something About Mary","Year":"1998","imdbID":"tt0129387","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BZWFlZjE5OTYtNWY0ZC00MzgzLTg5MjUtYTFkZjk2NjJkYjM0XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg"},{"Title":"Something Borrowed","Year":"2011","imdbID":"tt0491152","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BNzczNzMzODk0Nl5BMl5BanBnXkFtZTcwMjgwMjI0NA@@._V1_SX300.jpg"},{"Title":"And Now for Something Completely Different","Year":"1971","imdbID":"tt0066765","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BYWQzYjU5ODAtNDY5Yy00ZDIxLWJlMTEtOWRkMjlkNTdmMTBhXkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_SX300.jpg"},{"Title":"Life or Something Like It","Year":"2002","imdbID":"tt0282687","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BMTI3NjY5NTU3NV5BMl5BanBnXkFtZTYwMTcwNDU3._V1_SX300.jpg"},{"Title":"Something Wild","Year":"1986","imdbID":"tt0091983","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BMjE1MjI2MDc0NV5BMl5BanBnXkFtZTgwNjgzNDIxMDE@._V1_SX300.jpg"},{"Title":"Something New","Year":"2006","imdbID":"tt0437777","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BMzMzNzU0NzQ1NF5BMl5BanBnXkFtZTcwNTMzOTEzMQ@@._V1_SX300.jpg"},{"Title":"Something to Talk About","Year":"1995","imdbID":"tt0114496","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BZDhmOTczMjItMzg5NS00OTFiLWEzYTctMjAxMTZmMWVmMmQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg"},{"Title":"Something the Lord Made","Year":"2004","imdbID":"tt0386792","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BMTIzNTE0NjU4N15BMl5BanBnXkFtZTcwNjgyNDcyMQ@@._V1_SX300.jpg"},{"Title":"Something Wicked This Way Comes","Year":"1983","imdbID":"tt0086336","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BZjAwNWM2ZjItMTgwYi00YjMzLTkyZjEtYTU2YjFiODkzMjA5XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg"},{"Title":"There\'s Something Wrong with Aunt Diane","Year":"2011","imdbID":"tt2011325","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BN2Q3YTk0YTUtOTM4OC00NDdiLTg2ZTUtMzdiMDA2Njc5MmVlXkEyXkFqcGdeQXVyNzM0MDQ1Mw@@._V1_SX300.jpg"}],"totalResults":"1002","Response":"True"}'
'''