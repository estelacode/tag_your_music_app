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

        # 2. Actualizar metadatos en el fichero mp3 .
        self._model.update_metadata(updated_song)

        # 3. Limpiar los campos del formulario en la vista.
        self._view.clean_form_metatada()

        #4. Ocultar componente formulario en la vista.
        self._view.hide_form_component()

        #5. Añadir cancion con los metadatos ya actualizados al la lista de canciones.
        self._view.add_song(updated_song)


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

            # 2. Obtener path
            path = box_item.data(32)

            item = self._view.ui.list_songs.itemWidget(box_item)
            video_url = item.getVideoUrl()

            # 3. Reproducir cancion 
            if ".mp4" in video_url:
                self._view.play_and_stop_video(video_url)

            else:
                self._view.play_and_stop_song(path)
 
       
        

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



        