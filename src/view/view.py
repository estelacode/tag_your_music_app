
from PyQt5.QtWidgets import QMainWindow, QAction, QShortcut,QMenu
from PyQt5.QtCore import Qt
from view.gui_layout import App_MainWindow
from view.config import DEFAULT_MUSIC_DIR
from PyQt5.QtWidgets import  QFileDialog ,QListWidgetItem
from view.gui_custom_widget import QCustomQWidget
from PyQt5.QtGui import QPixmap, QKeySequence

import logging
logger = logging.getLogger(__name__)

class View(QMainWindow):

    def __init__(self):
        super().__init__()
        # Se instancia un objeto con todos los componentes y layouts de la UI
        self.ui = App_MainWindow() 
        # Se llama al metodo setup para crearlos en la vista
        self.ui.setup(self)
       
        # Ocultar botones de maximnizar, minimizar y cerrar de la venta de windows para usar los de la gui_layout.py
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # Lista de canciones de tipo song
        self.songs = []

    def minimize_view(self):
        """
    	Minimize the current view.
    	"""
        logger.debug("Called minimize_view method")
        self.showMinimized()


    def maximize_view(self):
        """
        Maximize the current view
        """
        logger.debug("Called maximize_view method")
        self.showMaximized()
    
    def restore_view(self):
        """
        Restore the current view
        """
        logger.debug("Called restore_view method")
        self.showNormal()

    def close_view(self):
        """
        Close the current view
        """
        logger.debug("Called close_view method")
        self.close()


    def load_song(self):
        """ 
        Carga una fichero de musica a la aplicacion. 
        Crea un objeto de tipo Song y lo añade a la lista interna.
        Crea un widget para añadirlo a la ListWidgetItem
        """
        # Seleccionar fichero mp3
        path, _ = QFileDialog.getOpenFileName(self, "Open Song", DEFAULT_MUSIC_DIR, "Sound Files (*.mp3 *.ogg *.wav *.m4a)") 
        logger.debug(f"Path del mp3 en la vista: {path}")
        return path
    

    def  display_item_song(self,song):    
        """
        Display a song item in the custom list widget.

        Args:
            song (Song): The song object to be displayed.

        This function creates a QCustomQWidget object to represent a song item in the custom list widget. It sets the cover image, title, artist, album, genre, and duration of the song item using the provided song object. It also sets the menu for the menu button of the song item using the `crear_menu` method of the QCustomQWidget object. The function connects the clicked signal of the menu button to the `open_menu` method of the QCustomQWidget object.
        The function then creates a QListWidgetItem object to represent the song item in the QListWidget. The size hint of the QListWidgetItem is set to the size hint of the QCustomQWidget object. Finally, the QListWidgetItem is added to the QListWidget and the QCustomQWidget object is set as the item widget for the QListWidgetItem.

        """
        # Create QCustomQWidget (Elementos de la lista custom)
        item = QCustomQWidget() #pos, lista de widges
        item.setCoverImg(song.coverImage)
        item.setTitle(song.title)
        item.setArtist(song.artist)
        item.setAlbum(song.album)
        item.setGenre(song.genre)
        item.setDuration(song.duration)
        item.btn_menu.setMenu(item.crear_menu(self.remove_item, self.edit_item, self.add_item_to_playlist))
        item.btn_menu.clicked.connect(item.open_menu)
      
        # Create QListWidgetItem (Elemento de la lista que contiene el elemento custom)
        box_item = QListWidgetItem(self.ui.list_songs)
        # Set size hint. Same size 
        box_item.setSizeHint(item.sizeHint()) 

        # Add QListWidgetItem into QListWidget
        self.ui.list_songs.addItem(box_item)
        self.ui.list_songs.setItemWidget(box_item, item)

    def add_item_to_playlist(self):
        pass

    def edit_item(self):
        """
        Edits an item in the list of songs.

        Retrieves the currently selected song from the list and populates the 
        corresponding text fields with the song's details.
        """
        pos = self.ui.list_songs.currentRow()
        if pos >= 0:
           song = self.songs[pos]
           self.ui.titleLineEdit.setText(song.title)
           self.ui.artistLineEdit.setText(song.artist)
           self.ui.albumLineEdit.setText(song.album)
           self.ui.genreLineEdit.setText(song.genre)
           self.ui.yearLineEdit.setText(song.release_date)
           self.ui.timeLineEdit.setText(song.duration)
           self.ui.trackLineEdit.setText(song.track_num)
           self.ui.videoLinkLineEdit.setText(song.url)
           self.ui.pathLinkLineEdit.setText(song.path)

    def remove_item(self):
        """
        Removes the currently selected item from the list of songs.

        This function retrieves the current row index of the selected item in the list of songs. 
        If the index is greater than or equal to 0, it removes the corresponding item widget from the list and updates the list widget.
        """
        pos = self.ui.list_songs.currentRow()
        if pos >= 0:
            self.ui.list_songs.removeItemWidget(self.ui.list_songs.takeItem(pos))   
