# 7.8
sandwich_orders = ['Big Mac', 'Mac Combo', 'Mac Chicken', 'Utra Chicken']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f'Ваш {sandwich} готов.')

print('Можете забрать свой заказ!')

# 7.9
sandwich_orders = [
    'Big Mac', 'pastrami', 'Mac Combo', 'pastrami', 'Mac Chicken', 'Utra Chicken', 'pastrami'
]
print('pastrami больше не осталось.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
