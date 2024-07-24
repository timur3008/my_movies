def get_category_result(category, movie):
    if category == 'series':
        return 'series' in movie    
    elif category == 'cartoons':
        return 'Мультфильм' in movie['genre']
    elif category == 'anime':
        return 'Аниме' in movie['genre']
    elif category == 'films':
        return 'series' not in movie and 'Мультфильм' not in movie['genre'] and 'Аниме' not in movie['genre']
    
def get_option_result(movie, **kwargs):
    temp = []

    if kwargs['genre'] != 'all':
        temp.append(kwargs['genre'] in movie['genre'])
    
    if kwargs['country'] != 'all':
        temp.append(kwargs['country'] == movie['country'])

    year = int(movie['year'])
    if kwargs['yearFrom'] != 0 and kwargs['yearTo'] != 0:
        temp.append(year >= kwargs['yearFrom'] and year <= kwargs['yearTo'])
    elif kwargs['yearFrom'] != 0:
        temp.append(year >= kwargs['yearFrom'])
    elif kwargs['yearTo'] != 0:
        temp.append(year <= kwargs['yearTo'])

    return all(temp)