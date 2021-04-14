import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class Test_room(unittest.TestCase):

    def setUp(self):

        self.room_01 = Room("Black Ace", 34)
        self.room_02 = Room("Urben Minute",71)
        self.room_03 = Room("Heart Box Karaoke", 20)
        self.room_04 = Room("Old Karaoke", 22)
        self.main_bar = Bar([self.room_01,self.room_02,self.room_03],self.room_04)
        self.guest_01 = Guest("Umair", 70, ["Wagon Wheel"])
        self.guest_02 = Guest("Muneeb", 90,[])
        self.guest_03 = Guest("Ali", 35,[])
        self.guest_04 = Guest("Ahmed", 77,[])

        self.song_01 = Song("Friends in Low Places", "Country")
        self.song_02 = Song("Wagon Wheel", "Country")
        self.song_03 = Song("I Wanna Dance with Somebody", "Pop")
        self.song_04 = Song("Mr. Brightside", "Pop")
        


# Room_initial_testing
    def test_room_01_created(self):
        self.assertEqual("Black Ace", self.room_01.name)

    def test_room_02_created(self):
        self.assertEqual("Urben Minute", self.room_02.name)


    def test_initial_room_capacity(self):
        self.assertEqual(2, self.room_01.room_capacity)

# Guest_checkin_testing
    def test_check_in_guest_01_room_01(self):
        self.room_01.guest_check_In(self.guest_01, self.main_bar)
        self.assertEqual(True, self.room_01.check_guest_in_guest_list(self.guest_01))
    
    def test_check_in_guest_02_room_02(self):
        self.room_02.guest_check_In(self.guest_02, self.main_bar)
        self.assertEqual(True, self.room_02.check_guest_in_guest_list(self.guest_02))


# Guest_CheckOut_testing
    def test_check_out_guest_01_room_01(self):
        self.room_01.guest_check_In(self.guest_01, self.main_bar)
        self.room_01.guest_check_In(self.guest_02, self.main_bar)
        self.room_01.guest_check_out(self.guest_01, self.main_bar)
        self.assertEqual(False, self.room_01.check_guest_in_guest_list(self.guest_01))
        self.assertEqual(f'Currently the Guest: {self.guest_01.name} is not in any room', self.main_bar.check_guest_total_spending(self.guest_01))

# Room_Capacity_testing
    def test_check_in_guest_01_room_02_full(self):
        self.room_02.guest_check_In(self.guest_01, self.main_bar)
        self.room_02.guest_check_In(self.guest_02, self.main_bar)
        additional_user = self.room_02.guest_check_In(self.guest_03, self.main_bar)
        self.assertEqual("The room is already full or closed",  additional_user) 


# Check_initial_playlist_for_guest_01_in_Room_01 

    def test_check_initial_playlist_in_room_01(self):
        self.room_01.guest_check_In(self.guest_01, self.main_bar)
        play_list =  self.room_01.check_play_list()
        self.assertEqual([], play_list)

# Add_first_song_to_the_playlist_and_check_1st_song

    def test_add_song_01_to_guest_01_in_room_01(self):
        self.room_01.guest_check_In(self.guest_01, self.main_bar)
        self.room_01.add_song_to_guest_play_list(self.song_01, self.guest_01)
        play_list =  self.room_01.check_play_list()
        self.assertEqual("Friends in Low Places", play_list[0])  

# Add_second_song_to_the_playlist_and_check_playlist

    def test_add_song_01_and_song_02_to_guest_01_in_room_01(self):
        self.room_01.guest_check_In(self.guest_01, self.main_bar)
        self.room_01.add_song_to_guest_play_list(self.song_01, self.guest_01)
        self.room_01.add_song_to_guest_play_list(self.song_02, self.guest_01)

        play_list =  self.room_01.check_play_list()
        self.assertEqual(['Friends in Low Places', 'Wagon Wheel'], play_list)  

#  Cant_add_song_to_play_list_without_guest_in_the_room

    def test_add_song_01_with_out_any_guest_in_room_01(self):
        added_song = self.room_01.add_song_to_guest_play_list(self.song_01, None)
        self.assertEqual("Please add the guest first in the room", added_song) 

# If_the_guest_dont_have_enough_money_to_enter_the_room

    def test_guest_03_wallent_not_enough_money_to_enter_room_01(self):
        wallet_status = self.room_02.guest_check_In(self.guest_03, self.main_bar)
        self.assertEqual(f'You do not have enough money to enter the room {self.room_02.name}', wallet_status )

# If_guest_favourite_song_is_added_to_paly_list

    def test_guest_01_favourite_song_being_played(self):
        self.room_01.guest_check_In(self.guest_01, self.main_bar)
        self.room_01.add_song_to_guest_play_list(self.song_01, self.guest_01)
        favourite_song = self.room_01.add_song_to_guest_play_list(self.song_02, self.guest_01)
        self.assertEqual("Whoo!", favourite_song)

# Each_customer_spending_track_by_main_bar       
    
    def test_each_customer_total_spendings(self):
        self.room_01.guest_check_In(self.guest_01, self.main_bar)
        self.room_03.guest_check_In(self.guest_01, self.main_bar)

        self.assertEqual("So far total spending for Guest: Umair is 54£", self.main_bar.check_guest_total_spending(self.guest_01))
