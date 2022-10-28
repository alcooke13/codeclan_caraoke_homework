import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Marty")

    def test_guest_has_name(self):
        self.assertEqual("Marty", self.guest1.name)
