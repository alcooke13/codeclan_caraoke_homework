import unittest
from classes.guest import Guest
from classes.food import Food

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Marty", 100, "Moments")
        self.guest2 = Guest("Kevin", 80, "Silence")
        self.food1 = Food("Pizza", 10)

    def test_guest_has_name(self):
        self.assertEqual("Marty", self.guest1.name)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest1.wallet)

    def test_reduce_guest_money(self):
        self.guest1.pay_fees(10)
        self.assertEqual(90, self.guest1.wallet)

    def test_guest_has_favorite_song(self):
        self.assertEqual("Moments", self.guest1.favorite_song)

    def test_guest_buys_food(self):
        self.guest1.pay_fees(10)
        self.assertEqual(90, self.guest1.wallet)
        self.guest1.buys_food("Pizza")
        self.assertEqual("Pizza", self.guest1.purchased_food[0]) ###
        self.assertEqual(1, len(self.guest1.purchased_food))


    def test_guest_total_bill_increases__and_wallet_goes_down(self): ###
        self.guest1.pay_fees(10)
        self.assertEqual(90, self.guest1.wallet)
        self.guest1.total_bill_goes_up(10)
        self.assertEqual(10, self.guest1.total_bill)
        
