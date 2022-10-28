import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Marty", 100, "Moments")
        self.guest2 = Guest("Kevin", 80, "Silence")

    def test_guest_has_name(self):
        self.assertEqual("Marty", self.guest1.name)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest1.wallet)

    def test_reduce_guest_money(self):
        self.guest1.pay_fees(10)
        self.assertEqual(90, self.guest1.wallet)

    def test_guest_has_favorite_song(self):
        self.assertEqual("Moments", self.guest1.favorite_song)
