class Bar:
    def __init__(self,live_rooms,closed_rooms):
        self.till = 0
        self.live_rooms=live_rooms
        self.full_rooms=[]
        self.closed_rooms=closed_rooms
        self.guests_spending={}

    def check_guest_spending(self, guest):
        return f'So far total spending for {guest.name} is {self.guests_spending.get(guest.name)}' 
    
    def each_guest_total_spending(self, guest, fare):
        if  guest.name in self.guests_spending:
            self.guests_spending[guest.name] = self.guests_spending.get(guest.name) + fare
        else:
            self.guests_spending[guest.name] = fare

    def update_till(self, room_fare):
        self.till += room_fare
