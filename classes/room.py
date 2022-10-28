class Room:
    
    def __init__(self, name):
        self.name = name
        self.space = []
        self.song_playlist = []

    def check_space(self):
        return len(self.space)

    def check_in_guest(self, guest_name):
        self.space.append(guest_name)

    def check_out_guest(self, guest_name):
        self.space.remove(guest_name)
    
    def add_song(self, song_name):
        self.song_playlist.append(song_name)