import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Fraser", 29)

    def test_guest_has_name(self):
        self.assertEqual("Fraser", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(29, self.guest.age)