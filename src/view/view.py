
from src.view.gui_layout import App_MainWindow
from src.view.gui_custom_widget import QCustomQWidget
from src.view.config import DEFAULT_MUSIC_DIR, PLAY_ICON, PAUSE_ICON
from src.utils.song import Song
from PyQt5.QtWidgets import  QFileDialog ,QListWidgetItem
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QByteArray, QBuffer, QIODevice, QUrl
from PyQt5.QtGui import QPixmap, QColor, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
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

        # Reproductor Mp3
        self.music_player = QMediaPlayer()

        # Reproductor Mp4
        self.video_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
   

        # sound Off
        self.on = False 
        


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


    def get_path_mp3(self):
        """ 
        Carga una fichero de musica a la aplicacion. 
        Crea un objeto de tipo Song y lo añade a la lista interna.
        Crea un widget para añadirlo a la ListWidgetItem
        """
        # Seleccionar fichero mp3
        path, _ = QFileDialog.getOpenFileName(self, "Open Song", DEFAULT_MUSIC_DIR, "Sound Files (*.mp3 *.ogg *.wav *.m4a)") 
        logger.debug(f"Path del fichero seleccionado en la vista: {path}")
        return path
    

    def show_component_form(self):
        """
        Displays the component form by showing the save form button, form layout content, 
        cover image content, and setting the style sheet for the container on the right.
        """
        self.ui.qfr_btn_save_form.show()
        self.ui.qfr_formLayout_content.show()
        self.ui.qfr_coverimage_content.show()
        self.ui.contenedor_derecho.setStyleSheet("background-color: rgb(255, 255, 255);") 

    def hide_form_component(self):
        """
        Hides the form component by hiding the save form button, form layout content, 
        cover image content, and setting the style sheet for the container on the right.
        """
        self.ui.qfr_btn_save_form.hide()
        self.ui.qfr_formLayout_content.hide()
        self.ui.qfr_coverimage_content.hide()
        #self.ui.contenedor_derecho.hide()
        self.ui.contenedor_derecho.setStyleSheet("background-color: rgb(234, 234, 234);") 
        
        

    def clean_form_metatada(self):
        """
        Cleans the metadata form by setting all text fields to an empty string and
        resetting the cover image to a white background.
        """

        self.ui.titleLineEdit.setText("")
        self.ui.artistLineEdit.setText("")
        self.ui.albumLineEdit.setText("")
        self.ui.genreLineEdit.setText("")
        self.ui.yearLineEdit.setText("")
        self.ui.timeLineEdit.setText("")
        self.ui.trackLineEdit.setText("")
        self.ui.videoLinkLineEdit.setText("")
        self.ui.pathLinkLineEdit.setText("") 

        pixmap = QPixmap(134,134)
        pixmap.fill(QColor("white"))  # Establece la imagen en blanco
        self.ui.lbl_cover_image.setPixmap(pixmap)
    
    
    def fill_form_metadata(self, song:Song):
        """
    	Fills the metadata form with information from a given Song object.

    	Parameters:
    	song (Song): The Song object containing the metadata to fill the form with.
    	"""
        
        self.ui.titleLineEdit.setText(song.title)
        self.ui.artistLineEdit.setText(song.artist)
        self.ui.albumLineEdit.setText(song.album)
        self.ui.genreLineEdit.setText(song.genre)
        self.ui.yearLineEdit.setText(song.release_date)
        self.ui.timeLineEdit.setText(song.duration)
        self.ui.trackLineEdit.setText(song.track_num)
        self.ui.videoLinkLineEdit.setText(song.video_url)
        self.ui.pathLinkLineEdit.setText(song.path) 

        if song.coverImage:
            pixmap = QPixmap()
            pixmap.loadFromData(song.coverImage)
            self.ui.lbl_cover_image.setPixmap(pixmap)
            

    def edit_cover_image(self):
        """
        Edits the cover image of the song by opening a file dialog for the user to select a new image.
        """
        imagePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "./assets/images")
        if imagePath: # si es la imagen es valida
            pixmap = QPixmap(imagePath)
            self.ui.lbl_cover_image.setPixmap(pixmap) # la muestro en el componente.
        
    def get_form_metadata(self)-> Song:
        """
    	Retrieves the metadata from the form fields and returns a new Song object.

    	Returns:
    	Song: A new Song object containing the metadata from the form fields.
    	"""

        new_title = self.ui.titleLineEdit.text()
        new_artist = self.ui.artistLineEdit.text()
        new_album =  self.ui.albumLineEdit.text()
        new_genre =  self.ui.genreLineEdit.text()
        new_release_date =  self.ui.yearLineEdit.text()
        new_time =  self.ui.timeLineEdit.text()
        new_track =  self.ui.trackLineEdit.text()
        video_url =  self.ui.videoLinkLineEdit.text()
        path = self.ui.pathLinkLineEdit.text()

        # get QPixmap from QLabel
        pixmap = self.ui.lbl_cover_image.pixmap()
        # convert QPixmap to bytes
        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.WriteOnly) 
        ok = pixmap.save(buff, "PNG")
        assert ok
        new_coverImage = ba.data()

        return Song(new_title, new_artist, new_album, new_genre,new_release_date, new_time,new_track, new_coverImage,path, video_url)


    def add_song(self,updated_song:Song):    
        """
        Display a song item in the custom list widget.

        Args:
            song (Song): The song object to be displayed.

        This function creates a QCustomQWidget object to represent a song item in the custom list widget. It sets the cover image, title, artist, album, genre, and duration of the song item using the provided song object. It also sets the menu for the menu button of the song item using the `crear_menu` method of the QCustomQWidget object. The function connects the clicked signal of the menu button to the `open_menu` method of the QCustomQWidget object.
        The function then creates a QListWidgetItem object to represent the song item in the QListWidget. The size hint of the QListWidgetItem is set to the size hint of the QCustomQWidget object. Finally, the QListWidgetItem is added to the QListWidget and the QCustomQWidget object is set as the item widget for the QListWidgetItem.

        """
        # Create QCustomQWidget (Elementos de la lista custom)
        item = QCustomQWidget() #pos, lista de widges
        item.setCoverImg(updated_song.coverImage)
        item.setTitle(updated_song.title)
        item.setArtist(updated_song.artist)
        item.setAlbum(updated_song.album)
        item.setGenre(updated_song.genre)
        item.setDuration(updated_song.duration)
        item.setVideoUrl(updated_song.video_url) # añadir ruta video mp4 (no se guarda en metadatos del mp3)
        item.btn_menu.setMenu(item.crear_menu(self.remove_item))
        #item.btn_menu.setMenu(item.crear_menu(self.remove_item, self.edit_item, self.add_item_to_playlist))
        item.btn_menu.clicked.connect(item.open_menu)
      
        # Create QListWidgetItem (Elemento de la lista que contiene el elemento custom)
        #box_item = QListWidgetItem(self.ui.list_songs)
        box_item = QListWidgetItem()
        # Añadir la ruta de la cancion seleccionada de forma independiente.
        box_item.setData(32, updated_song.path)

        # Set size hint. Same size 
        box_item.setSizeHint(item.sizeHint()) 

        # Add QListWidgetItem into QListWidget
        self.ui.list_songs.addItem(box_item)
        self.ui.list_songs.setItemWidget(box_item, item)


    def play_and_stop_song(self, path_mp3):
        url = QUrl.fromLocalFile(path_mp3)
        contenido = QMediaContent(url)
        self.music_player.setMedia(contenido)

        # Si esta apagada se encendera. Si esta sonando, se parará
        if  self.on == False:
            self.music_player.play()
            self.on = True
            #Animar icono play
            icon = QIcon()
            icon.addPixmap(QPixmap(PAUSE_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_play.setIcon(icon)
        else:
            self.music_player.stop()
            self.on = False
            #Animar icono play
            icon = QIcon()
            icon.addPixmap(QPixmap(PLAY_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_play.setIcon(icon)

    def play_and_stop_video(self,path_mp4):

        print("ruta_video:",path_mp4)
        url = QUrl.fromLocalFile(path_mp4)
        self.video_player.setMedia(QMediaContent(url))
        self.video_player.setVideoOutput(self.ui.qgv_video_content_middle)
        
        # play /stop video
        if  self.on == False:
            print("Play video...")
            self.video_player.play()
            self.on = True
            icon = QIcon()
            icon.addPixmap(QPixmap(PAUSE_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_play.setIcon(icon)
        else:
            print("Stop video...")
            self.video_player.stop()
            self.on = False
            #Animar icono play
            icon = QIcon()
            icon.addPixmap(QPixmap(PLAY_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_play.setIcon(icon)
        

    def remove_item(self):
        """
        Removes the currently selected item from the list of songs.
        """
       
        pos = self.ui.list_songs.currentRow()
        if pos >= 0:
            print("Calling remove item")
            # Borrar el item de la lista de pyq5
            box_item = self.ui.list_songs.takeItem(pos)
            self.ui.list_songs.removeItemWidget(box_item)   