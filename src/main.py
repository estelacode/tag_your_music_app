import sys
from PyQt5.QtWidgets import QApplication
from view.view import View
from model.model import Model
from controller.controller import Controller
import logging
import sqlite3



# Configurar el logging
logging.basicConfig(
    level=logging.DEBUG,  # Nivel de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato del log
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato de la fecha
    filename="app_log",  # Archivo de log.
    filemode='a'  # Modo de apertura del archivo (a: append, w: write)
)

# Obtener un logger
logger = logging.getLogger(__name__)

#  Punto de entrada  de la app
if __name__ == '__main__':
    logger.info("Running my app")

    # Conectar a la base de datos
    db_connection = sqlite3.connect('tagyourmusic.db')

    app = QApplication(sys.argv)
    modelo = Model()
    ventana =  View()
    controlador = Controller(ventana, modelo)
    ventana.show()
    sys.exit(app.exec_())