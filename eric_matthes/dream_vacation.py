poll = {}
places = []

name = input('Ваше имя: ')
name = str(name)
print(f'Здравствуйте, {name}, где бы Вы хотели провести свой отпуск?:')
print('Чтобы завершить опрос, введите exit')


while True:
    place = input('- ')
    if place == 'exit':
        poll[name] = places
        break

    places.append(place)


for name, places in poll.items():
    print(f'Места, где {name} провел бы свой отпуск:')
    for place in places:
        print(f'\t- {place}')
