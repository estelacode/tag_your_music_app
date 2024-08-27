import logging
import eyed3
from model.song import Song
logger = logging.getLogger(__name__)

class Controller:

    def __init__(self, view, model):
        # Atributo privado view que contiene una referencia a la vista instanciada en el fichero main.py
        self._view = view
        # Atributo privado model que contiene una referencia al modelo instanciado en el fichero main.py
        self._model = model
        self._connect_signals()

    def _add_song(self):
        """Adds a song to the application by loading its metadata and displaying it in the view"""

        # El metodo de la vista abre el modal para seleccionar el fichero mp3
        path = self._view.load_song()
        logger.debug(f"Path del mp3 en el controller: {path}")

        # necesito leer los metadatos del fichero con eyed3 -> model
        audiofile = self._model.load_metadata(path)
        song = self._model.mapperToSong(audiofile,path)
        self._view.songs.append(song)
        logger.debug(f"song: {song}")

        # necesito pintar el item de pyqt en la lista de items -> vista
        self._view.display_item_song(song)

    def _save_metadata_song(self):
        
        title = self._view.ui.titleLineEdit.text()
        artist = self._view.ui.artistLineEdit.text()
        album =  self._view.ui.albumLineEdit.text()
        genre =  self._view.ui.genreLineEdit.text()
        year =  self._view.ui.yearLineEdit.text()
        time =  self._view.ui.timeLineEdit.text()
        track =  self._view.ui.trackLineEdit.text()
        video =  self._view.ui.videoLinkLineEdit.text()
        path = self._view.ui.pathLinkLineEdit.text()
        logger.debug(f'{title, artist, album, genre, year, track}')

        # carga el fichero mp3
        audiofile = eyed3.load(path) 
        
        if audiofile.tag is None: # si el audifile tiene la tag a None
            audiofile.tag = eyed3.id3.Tag() # se le inicializa la tag
        audiofile.tag.title = title  #le asigna nuevo title
        audiofile.tag.artist = artist #le asigna nuevo artista
        audiofile.tag.album = album #le asigna nuevo album
        audiofile.tag.release_date = year  #le asigna release data
        audiofile.tag.genre = genre #le asigna nuevo genero
        
        if track:
            audiofile.tag.track_num = track # le asigna el  nuevo track
            
        # update del fichero mp3
        audiofile.tag.save() 
        #audiofile.tag.save(version=(1,None,None)) # For Explorer / Windows Media

        # Limpiar formulario
        self._view.ui.titleLineEdit.setText("")
        self._view.ui.artistLineEdit.setText("")
        self._view.ui.albumLineEdit.setText("")
        self._view.ui.genreLineEdit.setText("")
        self._view.ui.yearLineEdit.setText("")
        self._view.ui.timeLineEdit.setText("")
        self._view.ui.trackLineEdit.setText("")
        self._view.ui.videoLinkLineEdit.setText("")
        self._view.ui.pathLinkLineEdit.setText("")

        # Actualizar el objeto song que esta en la lista de canciones de la vista 
        songs = self._view.songs
        updated_song = Song(title, artist, album, genre, year, time, track,"",path, video)
        for i, s in enumerate(songs):
            if s.path == path:
                songs[i] = updated_song


    def _connect_signals(self):
        """
        Connects the signals of the view to the corresponding methods of the view.

        This method connects the clicked signal of the minimize button, maximize button,
        restore button, and close button of the view to their corresponding methods in the
        view. The minimize button is connected to the `minimize_view` method, the maximize
        button is connected to the `maximize_view` method, the restore button is connected
        to the `restore_view` method, and the close button is connected to the `close_view`
        method.

        """
        logger.debug("Called _connect_signals method")
        self._view.ui.btn_min.clicked.connect(self._view.minimize_view)
        self._view.ui.btn_max.clicked.connect(self._view.maximize_view)
        self._view.ui.btn_rest.clicked.connect(self._view.restore_view)
        self._view.ui.btn_close.clicked.connect(self._view.close_view)
        self._view.ui.btn_load_song.clicked.connect(self._add_song)
        self._view.ui.btn_save.clicked.connect(self._save_metadata_song)

        