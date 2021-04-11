class Bar:
    def __init__(self,live_rooms,closed_rooms):
        self.till = 0
        self.live_rooms=live_rooms
        self.closed_rooms=closed_rooms
        self.full_rooms=[]
        self.guests_spending={}

# Updating_till

    def update_till(self, room_fare):
        self.till += room_fare

# Adding_guest_spending

    def adding_guests_total_spending(self, guest, fare):
        if  guest.name in self.guests_spending:
            self.guests_spending[guest.name] = self.guests_spending.get(guest.name) + fare
        else:
            self.guests_spending[guest.name] = fare

# Removing_guest_spending

    def remove_guest_spending_info(self, guest):
        if guest.name in self.guests_spending:
            del self.guests_spending[guest.name]
        else:
            return f' The Guest {guest.name} has not been found'

# Checking_guest_spending

    def check_guest_total_spending(self, guest):
        if  guest.name not in self.guests_spending:
            return f'Currently the Guest: {guest.name} is not in any room'
        else:
            return f'So far total spending for Guest: {guest.name} is {self.guests_spending.get(guest.name)}£' 

