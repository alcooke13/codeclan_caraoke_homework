import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Moments")
        self.song2 = Song("A Beautiful Song")

    def test_song_has_name(self):
        self.assertEqual("Moments", self.song1.name)

    