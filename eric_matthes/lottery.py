from random import choice

lst = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'r', 'p', 'f', 'q')

win_ticket = ''
for i in range(4):
    win_ticket += f'|{str(choice(lst))}'

my_ticket = ''
i = 1
while my_ticket != win_ticket:
    my_ticket = ''
    for t in range(4):
        my_ticket += f'|{str(choice(lst))}'
    i += 1


print(f'ВЫИГРЫШНАЯ комбинация - {win_ticket}|')
print(f'ВАША комбинация - {my_ticket}|')
print(f'Потребовалось {i} ПОВТОРЕНИЙ цикла для получения выигрышной комбинации!')
