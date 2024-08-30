
from src.view.gui_layout import App_MainWindow
from src.view.gui_custom_widget import QCustomQWidget
from src.view.config import DEFAULT_MUSIC_DIR,DEFAULT_VIDEO_DIR, PLAY_ICON, PAUSE_ICON, LOW_VOLUME_ICON, MUTE_ICON, MID_VOLUME_ICON, HIGH_VOLUME_ICON
from src.utils.song import Song
from PyQt5.QtWidgets import  QFileDialog ,QListWidgetItem
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QByteArray, QBuffer, QIODevice, QUrl,pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

import logging

logger = logging.getLogger(__name__)

class View(QMainWindow):
    itemRemoved = pyqtSignal(int) #int es la posicion del elemento de la lista a borrar
      
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
        # video off
        self.video_on = False 

        self.volumen = 10 # Valor inicial del volumen (10%)

        self.pos_cancion_actual = -1
        self.pos_video_actual = -1


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
        self.ui.trackLineEdit.setText(str(song.track_num))
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

    def get_path_mp4(self):
        """ 
        Carga una fichero de musica a la aplicacion. 
        Crea un objeto de tipo Song y lo añade a la lista interna.
        Crea un widget para añadirlo a la ListWidgetItem
        """
        # Seleccionar fichero mp3
        path, _ = QFileDialog.getOpenFileName(self, "Path video", DEFAULT_VIDEO_DIR, "Sound Files (*.mp4 *.mov *.avi)") 
        logger.debug(f"Path del fichero mp4 seleccionado en la vista: {path}")
        if path:
            self.ui.videoLinkLineEdit.setText(path)
        
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

        return Song(-1,new_title, new_artist, new_album, new_genre,new_release_date, new_time,new_track, new_coverImage,path, video_url)


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
        item.setIdSong(updated_song.id)
        item.btn_close_song.clicked.connect(self.remove_item)
      
        # Create QListWidgetItem (Elemento de la lista que contiene el elemento custom)
        box_item = QListWidgetItem()
        # Añadir la ruta de la cancion seleccionada de forma independiente.
        box_item.setData(32, updated_song.path)

        # Set size hint. Same size 
        box_item.setSizeHint(item.sizeHint()) 

        # Add QListWidgetItem into QListWidget
        self.ui.list_songs.addItem(box_item)
        self.ui.list_songs.setItemWidget(box_item, item)


    def play_and_stop_song(self, path_mp3, pos, item):
        url = QUrl.fromLocalFile(path_mp3)
        contenido = QMediaContent(url)
        self.music_player.setMedia(contenido)

        # Si esta apagada se encendera. Si esta sonando, se parará
        if  self.on == False:
            print("Play song...")
            self.music_player.play()
            self.on = True
            #Animar icono play
            icon = QIcon()
            icon.addPixmap(QPixmap(PAUSE_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_play.setIcon(icon)
            self.show_label_song_on(item)
            self.pos_cancion_actual = pos
        else:
            print("Stop song...")
            self.music_player.stop()
            self.on = False
            #Animar icono play
            icon = QIcon()
            icon.addPixmap(QPixmap(PLAY_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_play.setIcon(icon)
            self.clean_label_song_on()
            self.pos_cancion_actual = -1



    def play_and_stop_video(self,path_mp4,pos, item):
        
        print("ruta_video:",path_mp4)
        url = QUrl.fromLocalFile(path_mp4)
        self.video_player.setMedia(QMediaContent(url))
        self.video_player.setVideoOutput(self.ui.qgv_video_content_middle)
        
        # play /stop video
        if  self.video_on == False:
            print("Play video...")
            self.video_player.play()
            self.video_on = True
            self.animate_pause_btn()
            self.show_label_song_on(item)
            self.pos_video_actual = pos
        else:
            print("Stop video...")
            self.video_player.stop()
            self.video_on = False
            self.animate_play_btn()
            self.clean_label_song_on()
            self.pos_video_actual = -1   
    
    def animate_pause_btn(self):
        """
        Animates the pause button by setting the icon to a pixmap of the pause icon.

        This function creates an instance of QIcon and sets its pixmap to the pause icon using QPixmap. The icon is then set as the icon for the 'btn_play' button in the user interface.
        """
        icon = QIcon()
        icon.addPixmap(QPixmap(PAUSE_ICON), QIcon.Normal, QIcon.Off)
        self.ui.btn_play.setIcon(icon)
        
    def animate_play_btn(self):
        """
        Animates the play button by setting the icon to a pixmap of the play icon.

        This function creates an instance of QIcon and sets its pixmap to the play icon using QPixmap. 
        The icon is then set as the icon for the 'btn_play' button in the user interface.
        """
        icon = QIcon()
        icon.addPixmap(QPixmap(PLAY_ICON), QIcon.Normal, QIcon.Off)
        self.ui.btn_play.setIcon(icon)

    def update_volume(self):
        """
        Updates the volume of the media players and animates the volume icon accordingly.

        Sets the minimum and maximum values of the horizontal slider to 0 and 100, respectively.
        Retrieves the current volume value from the slider and updates the volume of the video and music players if they are on.
        Animates the volume icon based on the current volume value, displaying mute, low, mid, or high volume icons.
        """
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(100)

        # Recuperar el valor de volumen del slider
        self.volumen = self.ui.horizontalSlider.value()


        # Si ek reproductor de video esta on, le cambio  el volumen 
        if self.video_on:
            self.video_player.setVolume(self.volumen)

        # Si el reproductor de musica esta on, le cambio el volumen
        if self.on:
            self.music_player.setVolume(self.volumen)

        # Animación del icono de sonido
        if self.volumen == 0:
            icon = QIcon()
            icon.addPixmap(QPixmap(MUTE_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_volumen.setIcon(icon)

        elif self.volumen <= 20:
            self.silencio = True
            icon = QIcon()
            icon.addPixmap(QPixmap(LOW_VOLUME_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_volumen.setIcon(icon)

        elif self.volumen <= 50:
            self.silencio = True
            icon = QIcon()
            icon.addPixmap(QPixmap(MID_VOLUME_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_volumen.setIcon(icon)
        else:
            self.silencio = True
            icon = QIcon()
            icon.addPixmap(QPixmap(HIGH_VOLUME_ICON), QIcon.Normal, QIcon.Off)
            self.ui.btn_volumen.setIcon(icon)

    def show_label_song_on(self, item):
        """
        Displays the title of the currently playing song on the UI label.

        Args:
            item: The song item containing the title to be displayed.
        """
        self.ui.lbl_info_song.setText("Reproduciendo 🎶💽: " + str(item.lbl_title_qvb.text())) 

    def clean_label_song_on(self):
        """
        Clears the text of the `ui.lbl_info_song` label.

        This function sets the text of the `ui.lbl_info_song` label to an empty string, effectively clearing any previous text that was displayed.
        """
        self.ui.lbl_info_song.setText("")    

    def remove_item(self):
        """
        Removes the currently selected item from the list of songs.

        This function removes the item at the current row of the `ui.list_songs` widget. 
        If the removed item is the currently playing song, the music player will be stopped. 
        If the removed item is the currently playing video, the video player will be stopped.
        """
       
        pos = self.ui.list_songs.currentRow()
        if pos >= 0:
            # Emite la posicion de la lista a eliminar
            self.itemRemoved.emit(pos)
 
        # Si borras la cancion que esta sonando se para el reproductor.
        if self.pos_cancion_actual == pos:
            self.music_player.stop()
            self.pos_cancion_actual = -1
            self.clean_label_song_on()
            self.animate_play_btn()

        # Si borras la cancion del video que esta sonando se para el reproductor de video.
        if self.pos_video_actual == pos:
            self.video_player.stop()
            self.pos_video_actual = -1
            self.clean_label_song_on()
            self.animate_play_btn()
