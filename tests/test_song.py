import unittest
from src.song import Song

class Test_song(unittest.TestCase):

    def setUp(self):

        self.song_01 = Song("song_01", "Country")
        self.song_02 = Song("song_02", "Country")
        self.song_03 = Song("song_03", "Pop")
        self.song_04 = Song("song_04", "Pop")


    def test_song_01_created(self):
        self.assertEqual("song_01", self.song_01.name)

    def test_song_02_created(self):
        self.assertEqual("song_02", self.song_02.name)

    def test_song_03_created(self):
        self.assertEqual("song_03", self.song_03.name)

    def test_song_04_created(self):
        self.assertEqual("song_04", self.song_04.name)