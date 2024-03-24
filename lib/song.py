
class Song:
    count = 0
    genres = []
    artists = {}
    genre_count = {}

    def __init__(self, name, artist, genre):

        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        self.add_artist_count(artist)
        self.genre_added(genre)

        
    def add_artist_count(self, artist):
       if artist not in Song.artists:
        Song.artists[artist] = 1

       else:
          Song.artists[artist] += 1


       if artist not in Song.artist_count:
        Song.artist_count[artist] = 1
       else:
        Song.artist_count[artist] += 1
    
    def genre_added(self, genre):
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
    