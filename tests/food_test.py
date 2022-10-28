import unittest
from classes.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food1 = Food("Pizza", 10)

    def test_food_has_name(self):
        self.assertEqual("Pizza", self.food1.name)

    def test_food_has_price(self):
        self.assertEqual(10, self.food1.price)