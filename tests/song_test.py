import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Never Gonna Give You Up", "Rick Astley")

    def test_song_has_name(self):
        self.assertEqual("Never Gonna Give You Up", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Rick Astley", self.song.artist)