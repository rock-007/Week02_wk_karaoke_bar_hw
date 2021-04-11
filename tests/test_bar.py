import unittest
from src.bar import Bar
from src.room import Room

class Test_bar(unittest.TestCase):
    
    def setUp(self):
        self.room_01 = Room("Black Ace", 34)
        self.room_02 = Room("Urben Minute",71)
        self.room_03 = Room("Heart Box Karaoke", 20)
        self.room_04 = Room("Old Karaoke", 10)
        self.main_bar =Bar([self.room_01,self.room_02, self.room_03], self.room_04)



# Live_room_testing

    def test_bar_live_rooms(self):
        self.assertEqual([self.room_01,self.room_02, self.room_03], self.main_bar.live_rooms)

# Full_room_testing
    def test_bar_full_rooms(self):
        self.assertEqual([], self.main_bar.full_rooms)

# closed_room_testing

    def test_bar_closed_rooms(self):
        self.assertEqual(self.room_04, self.main_bar.closed_rooms)



