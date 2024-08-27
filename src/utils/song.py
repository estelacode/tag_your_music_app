

class Song:
    
    def __init__(self, title, artist, album, genre, release_date, duration,track_num, coverImage,path_mp3,path_mp4=""):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.release_date = release_date
        self.duration = duration
        self.track_num = track_num
        self.coverImage = coverImage
        self.path_mp3 = path_mp3
        self.path_mp4 = path_mp4
      
    def __str__(self):
        """Sobrescribe el operador Str"""
        # Se omite coverImage:{self.coverImage} porque se imprime todo el binario de la imagen.
        return f"Song: (title:{self.title},artist:{self.artist},album:{self.album},genre:{self.genre},release_date:{self.release_date},duration:{self.duration},track_num:{self.track_num}, path_mp3:{self.path_mp3}, path_mp4:{self.path_mp4})."
