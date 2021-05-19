# 6.8
scuper = {
    'Вид': 'Кот',
    'Хозяин': 'Leonid'
}

korra = {
    'Вид': 'Собака',
    'Хозяин': 'Джерри'
}

tom = {
    'Вид': 'Кот',
    'Хозяин': 'Урлаг'
}

lets = [scuper, korra, tom]

for let in lets:
    kind = let['Вид']
    owner = let['Хозяин']
    print(f'Вид - {kind}, хозяин - {owner}')

# 6.9
favorite_places = {
    'Robin': ['Paris', 'Los-Santos'],
    'Салават': ['Chelyabinsk', 'Moscow'],
    'Roger': ['Dambldor', 'Potter'],
}

for name, places in favorite_places.items():
    print(f'Мой друг {name} и его любимые места:')
    for place in places:
        print('\t -', place.title())

# 6.11
cities = {
    'London': {
        'country': 'United Kingdom',
        'population': 17224782,
        'fact': 'dog',
    },
    'New York': {
        'country': 'USA',
        'population': 13226582,
        'fact': 'cat',
    },
    'Chicago': {
        'country': 'USA',
        'population': 922462,
        'fact': 'mouse',
    },
}

for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f'{city}:')
    print(f'\tcountry - {country}\n'
          f'\tpopulation - {population}\n'
          f'\tfact - {fact}')
