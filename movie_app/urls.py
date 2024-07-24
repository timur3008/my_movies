from django.urls import path
from .views import (
    home, 
    movies,
    current_movie,
    filter_country_movies,
    filter_genre_movies,
    filter_year_movies,
    actor_movie
)

urlpatterns = [
    path('', home, name='home'),
    path('content/<category>', movies, name='movies'),
    path('movie/<int:id>', current_movie, name='current_movie'),
    path('content/<category>/genre(<genre>)/country(<country>)/yearFrom(<int:yearFrom>)/yearTo(<int:yearTo>)', movies, name='current_filter_movie'),
    path('filter/country/<country>', filter_country_movies, name='filter_country_movies'),
    path('filter/genre/<genre>', filter_genre_movies, name='filter_genre_movies'),
    path('filter/year/<int:year>', filter_year_movies, name='filter_year_movies'),
    path('actor/<name>', actor_movie, name="actor_movie")
]
