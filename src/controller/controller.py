import logging
from src.utils.song import Song
from src.view.view import View
from src.model.model import Model
from pathlib import Path
logger = logging.getLogger(__name__)

class Controller:

    def __init__(self, view:View, model:Model):
        # Atributo privado view que contiene una referencia a la vista instanciada en el fichero main.py
        self._view = view
        # Atributo privado model que contiene una referencia al modelo instanciado en el fichero main.py
        self._model = model
        self._connect_signals()

    def load_song(self):
        """
        Loads a song into the application by retrieving its metadata and displaying it in the view.
        """

        # 1.Obtener el path de la cancion selecionada en la vista.
        path = self._view.get_path_mp3()

        if path:
            # 2. Extraer metadatos del fichero mp3 y guardarlos en un objeto de tipo Song.
            song = self._model.get_metadata(path)

            # 3. Mostrar componente formulario en la vista.
            self._view.show_component_form()

            # 4. Mostrar los campos rellenados con los metadatos de la cancion seleccionada.
            self._view.fill_form_metadata(song)
   
    
    def save(self):
        """
        Saves the modified song metadata by retrieving it from the form, updating it in the mp3 file, 
        cleaning the form metadata, hiding the form component, and adding the updated song to the song list.
        """
        

        # 1. Recuperar los metadatos modificados por el usuario en el formulario.
        updated_song = self._view.get_form_metadata()

        # 2. Actualizar metadatos en el fichero mp3.
        self._model.update_metadata(updated_song)

        # 3. Limpiar los campos del formulario en la vista.
        self._view.clean_form_metatada()

        #4. Ocultar componente formulario en la vista.
        self._view.hide_form_component()

        #5. Anadir la cancion a la base de datos
        id = self._model.create_song(updated_song)
        logger.debug("Se ha creado una cancion con el id:",id)

        #6. Añadir cancion con los metadatos ya actualizados al la lista de canciones.
        self._view.add_song(updated_song, id)

        



    def cancel(self):
        """
    	Cancels the current operation by cleaning the form metadata and hiding the form component in the view.
    	"""

        # 3. Limpiar los campos del formulario en la vista.
        self._view.clean_form_metatada()

        #4. Ocultar componente formulario en la vista.
        self._view.hide_form_component()

    def play_song(self):

        # 1. Recuperar la posicion de cancion seleccionada
        pos = self._view.ui.list_songs.currentRow()
        if  pos >=0:
            #box_item: <class 'QListWidgetItem'>
            box_item = self._view.ui.list_songs.item(pos)

            # 2. Obtener path y la url del video
            path = box_item.data(32)

            item = self._view.ui.list_songs.itemWidget(box_item)
            video_url = item.getVideoUrl()

            # 3. Reproducir cancion 
            if ".mp4" in video_url:
                self._view.play_and_stop_video(video_url, pos, item)
                
            else:
                self._view.play_and_stop_song(path, pos, item)
                

            
            
            
    
    def play_next_song(self):

        # Obtener el número de elementos
        num_items = self._view.ui.list_songs.count()

        # 1. Recuperar la posicion de cancion seleccionada
        pos = self._view.ui.list_songs.currentRow()

        #Next
        pos_next= pos +1

        if pos_next < num_items: #Controlar que no desborde por la cola de la derech
            # se convierte en el elemento actual de la lista
            self._view.ui.list_songs.setCurrentRow(pos_next)

            #box_item: <class 'QListWidgetItem'>
            box_item = self._view.ui.list_songs.item(pos_next)

            # 2. Obtener path
            path = box_item.data(32)

            item = self._view.ui.list_songs.itemWidget(box_item)
            video_url = item.getVideoUrl()

            # Como cambio de elemento de la lista paro todo significa:
            self._view.video_player.stop() # se para el video
            self._view.video_on = False # el video esta apagado
            self._view.music_player.stop()# se para el reproductor
            self._view.on = False # la musica esta apagada
            self._view.clean_label_song_on()# Borro la label de la cancion 
        
            # 3. Reproducir cancion 
            if ".mp4" in video_url:
                self._view.play_and_stop_video(video_url,pos_next, item)
            else:
                
                self._view.play_and_stop_song(path, pos_next, item)
        

    

    def play_previous_song(self):
          # Obtener el número de elementos
        num_items = self._view.ui.list_songs.count()

        # 1. Recuperar la posicion de cancion seleccionada
        pos = self._view.ui.list_songs.currentRow()

        #Next
        pos_prev= pos - 1
        
        if pos_prev >=0: # controlar que no desborde por la izquierdo
            # se convierte en el elemento actual de la lista
            self._view.ui.list_songs.setCurrentRow(pos_prev)

            #box_item: <class 'QListWidgetItem'>
            box_item = self._view.ui.list_songs.item(pos_prev)

            # 2. Obtener path
            path = box_item.data(32)

            item = self._view.ui.list_songs.itemWidget(box_item)
            video_url = item.getVideoUrl()

            self._view.video_player.stop()
            self._view.video_on = False
            self._view.music_player.stop()
            self._view.on = False
               
            # 3. Reproducir cancion 
            if ".mp4" in video_url:
                self._view.play_and_stop_video(video_url, pos_prev, item)
            else:
                
                self._view.play_and_stop_song(path, pos_prev, item)
    

    def remove_item_db(self, pos):
        """
    	Removes an item from the database and the view's list of songs.

    	Parameters:
    		pos (int): The position of the item to be removed.
    	"""

        # Obtener el elemento de la posicion pos
        box_item = self._view.ui.list_songs.item(pos)
     
        # Obtener el item de este box item
        item = self._view.ui.list_songs.itemWidget(box_item)

        # Obtener el id de este item
        id = item.id
        logger.debug("Se va a eliminar de la base de datos el elemento con id:",id)
        # Eliminar el elmento de la base de datos
        self._model.delete_song(id)
        
        # Elimina el item de la posicion pos en la lista de items de la vista
        self._view.ui.list_songs.takeItem(pos)
        

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
        self._view.ui.btn_load_song.clicked.connect(self.load_song)
        self._view.ui.btn_save.clicked.connect(self.save)
        self._view.ui.btn_cancel.clicked.connect(self.cancel)
        self._view.ui.btn_edit_coverimage.clicked.connect(self._view.edit_cover_image)
        self._view.ui.btn_play.clicked.connect(self.play_song)
        self._view.ui.btn_next.clicked.connect(self.play_next_song)
        self._view.ui.btn_previus.clicked.connect(self.play_previous_song)
        self._view.ui.btn_video.clicked.connect(self._view.get_path_mp4)
        self._view.ui.horizontalSlider.valueChanged.connect(self._view.update_volume)
        self._view.itemRemoved.connect(self.remove_item_db)

        