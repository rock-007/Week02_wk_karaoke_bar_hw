import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class Test_room(unittest.TestCase):

    def setUp(self):

        self.room_01 = Room("Black Ace")
        self.room_02 = Room("Urben Minute")
        # self.room_03 = Room("Heart Box Karaoke")
        # self.room_04 = Room("YoYo City Karaoke")
        self.guest_01 = Guest("Umair")
        self.guest_02 = Guest("Muneeb")
        self.song_01 = Song("Friends in Low Places", "Country")
        self.song_02 = Song("Wagon Wheel", "Country")
        self.song_03 = Song("I Wanna Dance with Somebody", "Pop")
        self.song_04 = Song("Mr. Brightside", "Pop")
        


# Room Initial testing
    def test_room_01_created(self):
        self.assertEqual("Black Ace", self.room_01.name)

    def test_room_02_created(self):
        self.assertEqual("Urben Minute", self.room_02.name)


    def test_initial_check_in_availability(self):
        self.assertEqual(True, self.room_01.check_in_availability)

# Guest CheckIn testing
    def test_check_in_guest_01_room_01(self):
        self.room_01.guest_check_In(self.guest_01)
        self.assertEqual(self.guest_01, self.room_01.guest)
    
    def test_check_in_guest_02_room_01_full(self):
        self.room_01.guest_check_In(self.guest_01)
        additional_user = self.room_01.guest_check_In(self.guest_02)
        self.assertEqual("The room is already occupied",  additional_user)   

    def test_check_in_guest_02_room_02(self):
        self.room_02.guest_check_In(self.guest_02)
        self.assertEqual(self.guest_02, self.room_02.guest)

# Room Capacity testing
    def test_check_in_guest_01_room_02_full(self):
        self.room_02.guest_check_In(self.guest_02)
        additional_user = self.room_02.guest_check_In(self.guest_01)
        self.assertEqual("The room is already occupied",  additional_user) 

    def test_check_in_guest_01_room_01_full(self):
        self.room_01.guest_check_In(self.guest_01)
        additional_user = self.room_01.guest_check_In(self.guest_02)
        self.assertEqual("The room is already occupied",  additional_user) 

# Check initial playlist for guest_01 in Room_01 

    def test_check_initial_playlist_in_room_01(self):
        self.room_01.guest_check_In(self.guest_01)
        play_list =  self.room_01.check_play_list()
        self.assertEqual([], play_list)

# add first song to the playlist and check 1st song

    def test_add_song_01_to_guest_01_in_room_01(self):
        self.room_01.guest_check_In(self.guest_01)
        self.room_01.add_song_to_guest_play_list(self.song_01)
        play_list =  self.room_01.check_play_list()
        self.assertEqual("Friends in Low Places", play_list[0])  

# add second song to the playlist and check playlist

    def test_add_song_01_and_song_02_to_guest_01_in_room_01(self):
        self.room_01.guest_check_In(self.guest_01)
        self.room_01.add_song_to_guest_play_list(self.song_01)
        self.room_01.add_song_to_guest_play_list(self.song_02)

        play_list =  self.room_01.check_play_list()
        self.assertEqual(['Friends in Low Places', 'Wagon Wheel'], play_list)  

#  cant add song to play list without guest in the room

    def test_add_song_01_with_out_any_guest_in_room_01(self):
        added_song = self.room_01.add_song_to_guest_play_list(self.song_01)
        self.assertEqual("Please add the guest first in the room", added_song)  