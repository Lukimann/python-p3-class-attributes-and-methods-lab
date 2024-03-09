
class Song:
    count = 0
    song = {}
    genres = []
    artists = {}

    def __init__(self, name, artist, genre):
        
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists[artist] = Song.artists.get(artist, 0) + 1

        if genre not in Song.genres:
          Song.genres.append(genre)



    @classmethod   
    def add_song_to_count(cls):
        return cls.count
    @classmethod
    def add_to_genres(cls):
        return cls.genres
    
    @classmethod
    def add_to_artists(cls):
        return cls.artists
        
song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")   
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
print(Song.add_song_to_count()) 
print(Song.genres)
