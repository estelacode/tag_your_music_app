
import eyed3
from time import gmtime
from time import strftime
from src.utils.song import Song
import logging
import sqlite3
logger = logging.getLogger(__name__)


class Model:
    
    def __init__(self):
    
        # Crear conexion a la base de datos. 
        self.con = sqlite3.connect('tagyourmusic.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        # Crear TABLE Canciones 
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Songs(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                              title VARCHAR,
                                                              artist  VARCHAR, 
                                                              album VARCHAR,
                                                              genre VARCHAR,
                                                              release_date INTEGER,
                                                              duration VARCHAR, 
                                                              track_num VARCHAR, 
                                                              coverImage BLOB,
                                                              path VARCHAR,   
                                                              video_url VARCHAR)""")
     
    
    def create_song(self, song:Song):
        
        title  = song.title
        artist = song.artist
        album =  song.album
        genre =  song.genre
        release_date = song.release_date
        duration = song.duration
        track_num = song.track_num
        coverImage = song.coverImage
        path= song.path
        video_url = song.video_url


        self.cur.execute(f"""INSERT INTO Songs(title, artist, album, genre, release_date, duration, track_num, coverImage, path, video_url)VALUES(?,?,?,?,?,?,?,?,?,?)""", (title, artist, album, genre, release_date, duration, track_num, coverImage, path, video_url))
        id = self.cur.lastrowid
        self.con.commit()
        return id

    def delete_song(self,id):
        self.cur.execute(f"""DELETE FROM Songs WHERE id={id}""")
        self.con.commit()

    def get_all_songs(self):
        self.cur.execute("""SELECT * FROM""")


    def get_metadata(self, path)->Song:
        """
        Retrieves metadata from an MP3 file.

        Parameters:
            path_mp3 (str): The path to the MP3 file.

        Returns:
            Song: An object containing the metadata of the MP3 file.
        """
        
        try:
            audiofile = eyed3.load(path)
        except Exception as e:
            logger.debug(f'Error:{e}')
        
        if audiofile.tag is None:
            audiofile.tag = eyed3.id3.Tag() 
        
        title = ""
        album = ""
        artist = ""
        genre = ""
        release_date = ""
        duration = ""
        track_num = ""
        coverImage = ""
        video_url= ""

        # Mapeo de datos. Extrear datos del objeto audiofile y lo guardo en variables.
        if audiofile.tag.title != None:
            title = audiofile.tag.title
        if audiofile.tag.artist != None:
            artist = audiofile.tag.artist
        if audiofile.tag.album != None:
            album = audiofile.tag.album
        if audiofile.tag.genre != None:
            genre = audiofile.tag.genre.name
        if audiofile.tag.release_date != None:
            release_date = str(audiofile.tag.release_date)
        if audiofile.info.time_secs != None:
            duration = strftime("%M:%S", gmtime(audiofile.info.time_secs))
        
        if audiofile.tag.comments != None:
           video_url =  ""#audiofile.tag.comments

        if audiofile.tag.track_num != None:
            # Must return a 2-tuple of (track-number, total-number-of-tracks)
            track_num = audiofile.tag.track_num[0]

        images = audiofile.tag.images
        for image in images:
            coverImage = image.image_data

       
        # Crear objeto song con dichas variables.
        return Song(title, artist, album, genre,release_date, duration,track_num, coverImage,path, video_url)

    def update_metadata(self, new_song:Song):
        # carga el fichero mp3
        audiofile = eyed3.load(new_song.path) 
        
        if audiofile.tag is None: # si el audifile tiene la tag a None
            audiofile.tag = eyed3.id3.Tag() # se le inicializa la tag
        audiofile.tag.title = new_song.title  #le asigna nuevo title
        audiofile.tag.artist = new_song.artist #le asigna nuevo artista
        audiofile.tag.album = new_song.album #le asigna nuevo album
        audiofile.tag.release_date = new_song.release_date  #le asigna release data
        audiofile.tag.images.set(3, new_song.coverImage , "image/jpg" ,u"Cover") #le asigna nueva cover
        audiofile.tag.genre = new_song.genre #le asigna nuevo genero
        #audiofile.tag.comments.set(new_song.video_url) # asignar url video youtube
        if new_song.track_num: 
            audiofile.tag.track_num = new_song.track_num
            
        # update del fichero mp3
        audiofile.tag.save() 
      
        