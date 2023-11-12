import unittest

from project.customers.models import Customer


class CustomerModelTest(unittest.TestCase):
    def test_customer_valid(self):
        book = Customer(name="Name Surname", city="City", age=18)
        self.assertEqual(book.name, "Name Surname")

    def test_name_invalid(self):
        with self.assertRaises(ValueError):
            Customer(name="<script>alert('XSS');</script>", city="City", age=18)

    def test_city_invalid(self):
        with self.assertRaises(ValueError):
            Customer(name="Name Surname", city="<script>alert('XSS');</script>", age=18)
