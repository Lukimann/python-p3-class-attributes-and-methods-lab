
class Song:
    count = 0
    song = {}
    genres = []
    artists = {}
    genre_count = {}

    def __init__(self, name, artist, genre):

        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists[artist] = Song.artists.get(artist, 0) + 1

        if artist not in Song.artists:
            Song.artists[artist] = 1
        else:
            Song.artists[artist] += 1

        if genre not in Song.genres:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1

    @classmethod   
    def add_song_to_count(cls):
        return cls.count
    @classmethod
    def add_to_genres(cls):
        return cls.genres
    
    @classmethod
    def add_to_artists(cls):
        return cls.artists
    
    @classmethod
    def add_to_genre_count(cls):
        return cls.genre_count