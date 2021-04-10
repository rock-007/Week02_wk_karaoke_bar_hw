class Room:
    def __init__(self, name, fare):
        self.name = name
        self.room_fare = fare
        self.guest = None
        self.playlist= None
        self.room_capacity = 2


    
    def guest_check_In(self, guest, bar):
        if  self in bar.live_rooms and self.room_capacity > 1 and guest.wallet >= self.room_fare :
            self.guest = guest
            self.playlist = []
            self.update_till_and_wallet(guest, bar)
            self.fill_up_room(bar)

            
        elif self in bar.live_rooms and self.room_capacity > 1:
            return f'You do not have enough money to enter the room {self.name}'    
        else:
            return "The room is already full or closed"
    
    def update_till_and_wallet(self, guest, bar):
        self.guest.wallet -= self.room_fare
        bar.each_guest_total_spending(guest, self.room_fare)
        bar.update_till(self.room_fare)
        #bar.till += self.room_fare


    def fill_up_room(self, bar):
        self.room_capacity -= 1
        if self.room_capacity < 1:
            bar.live_rooms.remove(self)
            bar.full_rooms.append(self)


    def check_play_list(self):
        return self.playlist
        
    def add_song_to_guest_play_list(self, song):
        if self.guest:
            self.playlist.append(song.name)
            if song.name in self.guest.favourite_song:
                return "Whoo!"
        else:
            return "Please add the guest first in the room"





