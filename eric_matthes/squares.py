# Генератор списка (list comprehension)
squares = [value**2 for value in range(1, 11)]
print(squares)


# Суммирование миллиона чисел
squares = list(range(1, 10**6 + 1))
print(sum(squares))


# Числа до 30, кратные 3-м
squares = list(range(3, 31, 3))
print(squares)


#  Создайте список первых 10 кубов
squares = [cub**3 for cub in range(1, 11)]
print(squares)
