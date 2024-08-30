

class Song:
    
    def __init__(self,id, title, artist, album, genre, release_date, duration,track_num, coverImage,path,video_url):
        self.id = id,
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.release_date = release_date
        self.duration = duration
        self.track_num = track_num
        self.coverImage = coverImage
        self.path = path
        self.video_url = video_url
      
    def __str__(self):
        """Sobrescribe el operador Str"""
        # Se omite coverImage:{self.coverImage} porque se imprime todo el binario de la imagen.
        return f"Song: (title:{self.title},artist:{self.artist},album:{self.album},genre:{self.genre},release_date:{self.release_date},duration:{self.duration},track_num:{self.track_num}, path:{self.path}, video_url:{self.video_url})."
