class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def display_songs(self):
        for song in self.songs:
            print(f"{song.title} by {song.artist}, duration: {song.duration} seconds")

class User:
    def __init__(self, username):
        self.username = username
        self.playlists = []

    def create_playlist(self, playlist):
        self.playlists.append(playlist)

    def display_playlists(self):
        for playlist in self.playlists:
            print(f"Playlist: {playlist.name}")
            playlist.display_songs()
            print()

class MusicPlayer:
    def __init__(self):
        self.songs = []
        self.playlists = []
        self.users = []

    def add_song(self, song):
        self.songs.append(song)

    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    def add_user(self, user):
        self.users.append(user)

    def display_songs(self):
        for song in self.songs:
            print(f"{song.title} by {song.artist}, duration: {song.duration} seconds")

    def display_playlists(self):
        for playlist in self.playlists:
            print(f"Playlist: {playlist.name}")

    def display_users(self):
        for user in self.users:
            print(f"User: {user.username}")

song1 = Song("Song 1", "Artist 1", 180)
song2 = Song("Song 2", "Artist 2", 240)
playlist1 = Playlist("Playlist 1")
playlist1.add_song(song1)
playlist1.add_song(song2)
user1 = User("User 1")
user1.create_playlist(playlist1)
music_player = MusicPlayer()
music_player.add_song(song1)
music_player.add_song(song2)
music_player.add_playlist(playlist1)
music_player.add_user(user1)
music_player.display_songs()
music_player.display_playlists()
music_player.display_users()
user1.display_playlists()