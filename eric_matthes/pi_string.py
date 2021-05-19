with open('pi_million_digits.txt') as file_object:
    """Чтение всего файла."""
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

my_birth = input('Введите свою дату рождения в формате ддммгг: ')
if my_birth in pi_string:
    print('Ваш день рождения отображается в первом миллионе цифр числа Пи!')
else:
    print('Ваш день рождения не входит в число первых миллионов цифр числа пи.')
