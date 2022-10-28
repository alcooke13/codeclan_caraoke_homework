class Room:
    
    def __init__(self, name, till):
        self.name = name
        self.space = []
        self.song_playlist = []
        self.till = till
        self.menu = []

    def check_space(self):
        return len(self.space)

    def check_in_guest(self, guest_name):
        if self.check_space() < 2:
            self.space.append(guest_name)
        return "Sorry. Room is full"

    def check_out_guest(self, guest_name):
        self.space.remove(guest_name)
    
    def add_song(self, song_name):
        self.song_playlist.append(song_name)

    def add_to_till(self, amount):
        self.till += amount

    def guest_finds_favorite_song(self, song_name):
        for song in self.song_playlist:
            if song == song_name:
                return "Woohoo!"

    def add_food_to_menu(self, food):
        self.menu.append(food)
        
