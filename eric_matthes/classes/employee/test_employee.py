import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Frank', 'Ocean', 120_000)

    def test_give_default_raise(self):
        """Увеличение ежегодного оклада по умолчанию на $5000"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 125_000)

    def test_give_custom_raise(self):
        """Увеличение ежегодного оклада на $10000"""
        self.employee.give_raise(10_000)
        self.assertEqual(self.employee.annual_salary, 130_000)


if __name__ == '__main__':
    unittest.main()
