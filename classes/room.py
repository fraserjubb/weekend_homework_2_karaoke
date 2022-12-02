class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.playlist = []

    def guest_list_length(self):
        return len(self.guest_list)

    def add_guest_to_list(self, guest):
        self.guest_list.append(guest)        

    def remove_guest_from_list(self, guest):
        self.guest_list.remove(guest)

    def playlist_length(self):
        return len(self.playlist)

    def add_songs_to_playlist(self, song):
        self.playlist.append(song)        
     
    def remove_songs_from_playlist(self, song):
        self.playlist.remove(song)        
     

    # def check_guest_list(self):
    #     return self.guest_list