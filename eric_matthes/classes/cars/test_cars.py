import unittest
from car import Car
from electric_car import ElectricCar as EC


class CarsTestCase(unittest.TestCase):
    def setUp(self):
        self.my_beetle = Car('volkswagen', 'beetle', 2019)
        self.my_tesla = EC('tesla', 'roadster', 2019)

    def test_descriptive_name_cars(self):
        self.assertEqual(self.my_beetle.get_descriptive_name(), '2019 Volkswagen Beetle')
        self.assertEqual(self.my_tesla.get_descriptive_name(), '2019 Tesla Roadster')

    def test_read_odometer(self):
        self.assertEqual(self.my_beetle.read_odometer(), 'This car has 0 miles on it.')
        self.assertEqual(self.my_tesla.read_odometer(), 'This car has 0 miles on it.')


if __name__ == '__main__':
    unittest.main()
