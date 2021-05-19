from random import randint


class Die:
    """Класс, представлящий кубик."""

    def __init__(self, sides=6):
        """По умолчанию используется шестригранный кубик."""
        self.sides = sides

    def roll(self):
        """Возвращает случайное число от 1 до числа граней."""
        return randint(1, self.sides)

