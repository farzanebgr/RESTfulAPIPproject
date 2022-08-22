"""RESTfulAPIPproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from watch_list_app.api.views import WatchListAV, WatchListDetailsAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
   path('watchlist/', WatchListAV.as_view(), name='watch-list'),
   path('watchlist/<int:pk>', WatchListDetailsAV.as_view(), name='watch-list-details'),
   path('platform/', StreamPlatformAV.as_view(), name='stream-platform-list'),
   path('platform/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-platform-detail'),
]

# from watch_list_app.api.views import movie_list, movie_details
# from watch_list_app.api.views import MovieListAV,MovieDetailsAV
# urlpatterns = [
#    path('list/', movie_list, name='movie-list'),
#    path('<int:pk>', movie_details, name='movie-details'),
#    path('list/', MovieListAV.as_view(), name='movie-list'),
#    path('<int:pk>', MovieDetailsAV.as_view(), name='movie-detail'),
# ]
