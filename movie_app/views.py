from django.shortcuts import render
from .movies import datas
from .future import get_category_result, get_option_result


def home(request):
    return render(request, 'home.html')

def movies(request, category, genre = 'all', country = 'all', yearFrom = 0, yearTo = 0):
    movies = []
    genres = []
    years = set()
    yearsTo = set()
    countries = set()
    for id, item in enumerate(datas):
        movie = {
            'name': item['ru_name'],
            'genre': item['genre'][0],
            'year': item['year'],
            'url': item['small_image'],
            'id': id
        }
        is_category = get_category_result(category, item)
        is_options = get_option_result(item, genre=genre, country=country, yearFrom=yearFrom, yearTo=yearTo)

        years.add(str(item['year']))
        genres.extend(item['genre'])
        countries.add(item['country'])

        if is_category and is_options:
            yearsTo.add(str(item['year']))
            movies.append(movie)


    return render(request, 'movies.html', { 
        'movies': movies, 
        'genres': sorted(set(genres)),
        'years': sorted(years, reverse=True),
        'yearsTo': sorted(yearsTo, reverse=True),
        'countries': sorted(countries)
        })

def current_movie(request, id=0):
    cur = datas[id]
    movie = {
        'poster': cur['big_image'],
        'ruName': cur['ru_name'],
        'enName': cur['en_name'],
        'imbd': cur['imbd'],
        'kp': cur['kp'],
        'limit': cur['limit'],
        'year': cur['year'],
        'country': cur['country'],
        'genres': cur['genre'],
        'description': cur['description'],
        'actors': cur['actors'],
        'directors': cur['directors'],
        'writers': cur['writers'],
        'producers': cur['producers'],
        'screens': cur['screens']
    }

    return render(request, 'movie.html', { 'movie': movie })


def filter_country_movies(request, country):
    return render(request, 'filter_movies.html')

def filter_genre_movies(request, genre):
    return render(request, 'filter_movies.html')

def filter_year_movies(request, year):
    return render(request, 'filter_movies.html')

def actor_movie(request, name):
    return render(request, 'actor.html')