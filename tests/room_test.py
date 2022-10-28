import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("CodeClan Caraoke")
        self.guest1 = Guest("Marty")
        self.song1 = Song("A Beautiful Song")
        self.song2 = Song("Moments")

    def test_room_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.room1.name)

    def test_space_is_empty(self):
        self.assertEqual(0, self.room1.check_space())

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1.name)
        self.assertEqual(1, len(self.room1.space))

    def test_check_out_guests(self):
        self.room1.check_in_guest(self.guest1.name)
        self.room1.check_out_guest(self.guest1.name)
        self.assertEqual(0, len(self.room1.space))

    def test_add_song_to_playlist(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.song_playlist))
        # self.room1.add_song(self.song2)
        # self.assertEqual(2, len(self.room1.song_playlist))


