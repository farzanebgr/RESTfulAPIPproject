from django.shortcuts import render
from IDBM_app.models import Movie
from django.http import JsonResponse


# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'data': list(movies.values())
    }
    return JsonResponse(data)
