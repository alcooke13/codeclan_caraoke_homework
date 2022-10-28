import unittest
from classes import food
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.food import Food

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("CodeClan Caraoke", 500)
        self.guest1 = Guest("Marty", 100, "Moments")
        self.guest2 = Guest("Kevin", 80, "Silence")
        self.guest3 = Guest("Seli", 90, "Foundations")
        self.song1 = Song("A Beautiful Song")
        self.song2 = Song("Moments")
        self.food1 = Food("Pizza", 10)
        self.food2 = Food("Burger", 7)

    def test_room_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.room1.name)

    def test_space_is_empty(self):
        self.assertEqual(0, self.room1.check_space())

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1.name)
        self.assertEqual(1, len(self.room1.space))

    def test_check_in_guest_2(self):
        self.room1.check_in_guest(self.guest1.name)
        self.room1.check_in_guest(self.guest2.name)
        self.assertEqual(2, len(self.room1.space))

    def test_check_in_guest_over_2(self):
        self.room1.check_in_guest(self.guest1.name)
        self.room1.check_in_guest(self.guest2.name)
        self.assertEqual("Sorry. Room is full",  self.room1.check_in_guest(self.guest3.name))
        

    def test_check_out_guests(self):
        self.room1.check_in_guest(self.guest1.name)
        self.room1.check_out_guest(self.guest1.name)
        self.assertEqual(0, len(self.room1.space))

    def test_add_song_to_playlist(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.song_playlist))
        self.room1.add_song(self.song2)
        self.assertEqual(2, len(self.room1.song_playlist))

    def test_add_money_to_till(self):
        self.room1.add_to_till(10)
        self.assertEqual(510, self.room1.till)

    def test_guest_favorite_song(self):
        self.room1.add_song(self.song1.name)
        self.room1.add_song(self.song2.name)
        self.assertEqual("Woohoo!", self.room1.guest_finds_favorite_song(self.song2.name))

    def test_add_food_to_menu(self):
        self.room1.add_food_to_menu(self.food1)
        self.assertEqual(1, len(self.room1.menu))
