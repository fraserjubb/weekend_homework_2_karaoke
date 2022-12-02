import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Karaoke Classics")
        self.guest_list_1 = []
        self.guest_1 = Guest("Fraser", 29)
        self.guest_2 = Guest("Shrek", 40)
        self.song_1 = Song("Never Gonna Give You Up", "Rick Astley")
        self.song_2 = Song("500 Miles", "The Proclaimers")
        self.playlist_1 = {}

    def test_room_has_name(self):
        self.assertEqual("Karaoke Classics", self.room.name)

    def test_add_guests_to_room(self):
        self.room.add_guest_to_list(self.guest_1)
        self.room.add_guest_to_list(self.guest_2)
        self.assertEqual(2, self.room.guest_list_length())

    def test_remove_guests_from_list(self):
        self.room.add_guest_to_list(self.guest_1)
        self.room.add_guest_to_list(self.guest_2)
        self.room.remove_guest_from_list(self.guest_1)
        self.assertEqual(1, self.room.guest_list_length())

    def test_add_songs_to_playlist(self):
        self.room.add_songs_to_playlist(self.song_1)
        self.room.add_songs_to_playlist(self.song_2)
        self.assertEqual(2, self.room.playlist_length())

    def test_remove_songs_from_playlist(self):
        self.room.add_songs_to_playlist(self.song_1)
        self.room.add_songs_to_playlist(self.song_2)
        self.room.remove_songs_from_playlist(self.song_2)
        self.assertEqual(1, self.room.playlist_length())
# 
    # def test_check_guest_list(self):
    #     self.assertEqual(self.guest_list_1, self.room.guest_list)
