import random

guess = ''

print('Угадайте результат подбрасывания монеты! Введите орел или решка:')
while guess not in ('орел', 'решка'):
    guess = input()

    if guess == 'орел':
        guess = 1
    elif guess == 'решка':
        guess = 0

    toss = random.randint(0, 1)  # 0 - решка, 1 - орел
    if toss == guess:
        print('Есть!')
    else:
        print('Увы! Попробуйте снова!')
        continue
