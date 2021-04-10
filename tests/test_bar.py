import unittest
from src.bar import Bar
from src.room import Room

class Test_bar(unittest.TestCase):
    
    def setUp(self):
        self.room_01 = Room("Black Ace", 34)
        self.room_02 = Room("Urben Minute",71)
        self.room_03 = Room("Heart Box Karaoke", 20)
        self.main_bar =Bar([self.room_01,self.room_02],self.room_03)





    def test_bar_live_rooms(self):
        self.assertEqual([self.room_01,self.room_02], self.main_bar.live_rooms)
        
    def test_bar_full_rooms(self):
        self.assertEqual([], self.main_bar.full_rooms)

    def test_bar_closed_rooms(self):
        self.assertEqual(self.room_03, self.main_bar.closed_rooms)

