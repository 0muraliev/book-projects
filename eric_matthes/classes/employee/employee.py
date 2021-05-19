"""Класс для представления работника."""


class Employee:
    """Модель работника"""
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary

    def give_raise(self, amount_raise=5000):
        """По умолчанию увеличивает ежегодный оклад на $5000"""
        self.annual_salary += amount_raise
        return self.annual_salary
