from pathlib import Path
import eyed3
from time import gmtime
from time import strftime
from model.song import Song
class Model:
    
    def __init__(self):
        pass        
        
    def load_metadata(self,path:str):
        """
    	Loads the metadata of an audio file identified by the given path.
    
    	Parameters:
    	path (str): The path to the audio file.
    
    	Returns:
    	eyed3.core.AudioFile: A concrete type of AudioFile containing the metadata of the audio file.
    	"""
        audiofile = eyed3.load(path)    

        if audiofile.tag is None:
            audiofile.tag = eyed3.id3.Tag()
        
        return audiofile
    
    def mapperToSong(self, audiofile, path):
        title = ""
        album = ""
        artist = ""
        genre = ""
        release_date = ""
        duration = ""
        track_num = ""
        coverImage = ""

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

        if audiofile.tag.track_num != None:
            # Must return a 2-tuple of (track-number, total-number-of-tracks)
            track_num = audiofile.tag.track_num[0]

        images = audiofile.tag.images
        for image in images:
            coverImage = image.image_data

        # Crear objeto song con dichas variables.
        return Song(title, artist, album, genre,release_date, duration,track_num, coverImage,path,"")

