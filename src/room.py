class Room:
    def __init__(self, name):
        self.name = name
        self.guest = None
        self.check_in_availability = True
        self.playlist= None


    
    def guest_check_In(self, guest):
        if  self.check_in_availability:
            self.guest = guest
            self.check_in_availability = False
            self.playlist = []
        else:
            return "The room is already occupied"

    def check_play_list(self):
        return self.playlist
        
    def add_song_to_guest_play_list(self, song):
        if self.guest:
            self.playlist.append(song.name)
        else:
            return "Please add the guest first in the room"

        
    


