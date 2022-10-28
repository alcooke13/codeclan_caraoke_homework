import unittest
from classes.bill import Bill
from classes.food import Food

class TestBill(unittest.TestCase):
    def setUp(self):
        self.bill_1 = Bill("Marty")
        self.food_1 = Food("Pizza", 10)

    def test_bill_has_name(self):
        self.assertEqual("Marty", self.bill_1.customer_name)

    def test_bill_starts_at_0(self):
        self.assertEqual(0, self.bill_1.total_bill)