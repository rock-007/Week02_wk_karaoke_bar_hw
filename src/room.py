class Room:
    def __init__(self, name, room_fare):
        self.name = name
        self.room_fare = room_fare
        self.guest_list = []
        self.playlist= None
        self.room_capacity = 2

# Check_in

    def guest_check_In(self, guest, bar):
        if  self.room_status(bar) and self.guest_status(guest):
            self.update_guest_list(guest)
            self.playlist = []
            self.update_till(guest, bar)
            self.update_wallet(guest, bar)
            self.update_bar_guest_spending(guest, bar)
            self.fill_up_room(bar)
        elif self in bar.live_rooms and self.room_capacity > 1:
            return f'You do not have enough money to enter the room {self.name}'    
        else:
            return "The room is already full or closed"

    def room_status(self, bar):
        return (self in bar.live_rooms and self.room_capacity > 1)
    
    def guest_status(self,guest):
        return guest.wallet >= self.room_fare and not self.check_guest_in_guest_list(guest)
    
    def check_guest_in_guest_list(self, guest):
        return guest in self.guest_list

    def update_guest_list(self,guest):
        self.guest_list.append(guest)
    
    def update_till(self, guest, bar):
        bar.update_till(self.room_fare)

    def update_wallet(self, guest, bar):
        guest.update_wallet(self.room_fare)
    
    def update_bar_guest_spending(self, guest, bar):
        bar.adding_guests_total_spending(guest, self.room_fare)
    
    def fill_up_room(self, bar):
        self.room_capacity -= 1
        if self.room_capacity < 1:
            bar.live_rooms.remove(self)
            bar.full_rooms.append(self)

#Check_out

    def guest_check_out(self, guest, bar):
        if guest in self.guest_list:
            self.guest_list.remove(guest)
            bar.remove_guest_spending_info(guest)

# Add_songs_to_play_list

    def add_song_to_guest_play_list(self, song, guest):

        if guest in self.guest_list:
            self.playlist.append(song.name)
            if song.name in guest.favourite_song:
                return "Whoo!"
        else:
            return "Please add the guest first in the room"    

# Check_guest_in_guest_list

    def check_guest_in_guest_list(self, guest):
        if guest in self.guest_list:
            return True
        else:
            return False

# Check_play_list

    def check_play_list(self):
        return self.playlist


