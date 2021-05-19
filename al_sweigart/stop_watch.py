import time

# Отображение инструкции по использованию программы.
print('''
Чтобы начать отсчет, нажмите ENTER.
Впоследствии для имитации щелчков кнопки секундомера нажимайте клавишу ENTER.
Для выхода из программы нажмите клавиши <Ctrl + C>.
'''.center(321, '-'))

# Нажатие клавиши Enter начинает отсчет
input()

print('Отсчет начат.')
start_time = time.time()
last_time = start_time

# Количество кругов.
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f'Круг #{lap_num}'.center(20, '-'),
              f'\n{total_time} ({lap_time})')
        lap_num += 1
        # Обновление времени последнего замера.
        last_time = time.time()

except KeyboardInterrupt:
    print('\nГотово.')
