import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Marty", 100)

    def test_guest_has_name(self):
        self.assertEqual("Marty", self.guest1.name)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest1.wallet)
