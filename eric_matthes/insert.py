# Изменение списка гостей
guest_list = ['Bob', 'Leroi', 'Yan']
print(f'Не сможет прийти - {guest_list.pop()}')
guest_list.append('Den')


# Больше гостей
guest_list.insert(0, 'Digma')
guest_list.insert(1, 'Fedya')
guest_list.append('Sasanya')
print('На обед приглашаются всего два гостя ):')

while not len(guest_list) == 2:
    print(f'{guest_list.pop()}, я сожалею об отмене приглашения...')

for g in guest_list:
    print(f'Дорогой {g}, приглашаю тебя на вечеринку друзей, приходи!')

print(f'Приглашено всего {len(guest_list)} гостя.')
del guest_list[0]
del guest_list[0]

print(guest_list)
