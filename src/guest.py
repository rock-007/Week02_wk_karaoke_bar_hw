class Guest:

    def __init__(self, name, wallet, favourite_song ):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

#Update_wallet

    def update_wallet(self, room_fare):
        self.wallet -= room_fare
