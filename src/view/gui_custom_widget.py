
from ctypes import alignment
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import  pyqtSignal
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QMenu
from PyQt5.QtGui import QPixmap,QIcon
from src.view.config import COVER_IMG_DEFAULT

class QCustomQWidget(QWidget):
    """  Class QCustomQWidget
    Custom QWidget with a horizontal layout containing several vertical layouts and labels for displaying song information.
    """
    clicked =  pyqtSignal(int)
      
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
    
        self.qhbox_main_content = QHBoxLayout()
    
        self.qvbox_0 = QVBoxLayout()
        self.lbl_icon_cover_img = QLabel()
        self.qvbox_0.addWidget(self.lbl_icon_cover_img)
        
        self.qvbox_1 = QVBoxLayout()
        self.lbl_title_qvb = QLabel()
        self.lbl_title_qvb.setFont(QtGui.QFont("Calibri", 10, QtGui.QFont.Bold))
        self.lbl_title_qvb.setFixedHeight(12)
        self.lbl_title_qvb.setAlignment(QtCore.Qt.AlignLeft)
              
        self.lbl_artist_qvb= QLabel()
        self.lbl_artist_qvb.setFont(QtGui.QFont("Calibri", 10))
        self.lbl_artist_qvb.setFixedHeight(12)
        self.lbl_artist_qvb.setAlignment(QtCore.Qt.AlignLeft)
       

        self.qvbox_1.addWidget(self.lbl_title_qvb)
        self.qvbox_1.addWidget(self.lbl_artist_qvb)
        self.qvbox_1.setSpacing(0)
        
        
        # BOX 2
        self.qvbox_2 = QVBoxLayout()
        self.lbl_album_qvb = QLabel()
        self.lbl_album_qvb.setFont(QtGui.QFont("Calibri", 10))
        self.lbl_album_qvb.setFixedHeight(15)
        self.qvbox_2.addWidget(self.lbl_album_qvb)
        
        # BOX 3
        self.qvbox_3 = QVBoxLayout()
        self.lbl_genre_qvb = QLabel()
        self.lbl_genre_qvb.setFont(QtGui.QFont("Calibri", 10))
        self.lbl_genre_qvb.setFixedHeight(15)
        self.qvbox_3.addWidget(self.lbl_genre_qvb)
        
        # BOX 4
        self.qvbox_4 = QVBoxLayout()
        self.lbl_duration_qvb = QLabel()
        self.lbl_duration_qvb.setFont(QtGui.QFont("Calibri", 10))
        self.lbl_duration_qvb.setFixedHeight(12)
        self.qvbox_4.addWidget(self.lbl_duration_qvb)
        
         # BOX 5 : Menu de la cancion
        self.qvbox_5 = QVBoxLayout()
        self.btn_menu = QPushButton()
        #icon = QIcon()
        #icon.addPixmap(QPixmap(MENU_ITEM_SONG_ICON), QIcon.Normal, QIcon.Off)
        #self.btn_menu.setIconSize(QtCore.QSize(25, 25))
        #self.btn_menu.setIcon(icon)      
        self.qvbox_5.addWidget(self.btn_menu)
       
               
        self.qhbox_main_content.addLayout(self.qvbox_0) # add box1  to qhbox_main_content
        self.qhbox_main_content.addLayout(self.qvbox_1) # add box1  to qhbox_main_content
        self.qhbox_main_content.addLayout(self.qvbox_2) # add box2  to qhbox_main_content
        self.qhbox_main_content.addLayout(self.qvbox_3) # add box3  to qhbox_main_content
        self.qhbox_main_content.addLayout(self.qvbox_4) # add box4  to qhbox_main_content
        self.qhbox_main_content.addLayout(self.qvbox_5) # add box5  to qhbox_main_content
        
        self.setLayout(self.qhbox_main_content)
        
        # setStyleSheet
        "#lbl_title_qvb {}\n"

        
        self.lbl_title_qvb.setStyleSheet('''
            background-color: transparent; color: rgb(0, 0, 0); margin: 0px; padding:0px;
        ''')
        self.lbl_artist_qvb.setStyleSheet('''
            background-color: transparent;color: rgb(0, 0, 0); margin: 0px; padding:0px;
        ''')
        
        self.lbl_album_qvb.setStyleSheet('''
            background-color: transparent;color: rgb(0, 0, 0);margin: 0px; padding:0px;
        ''')
        self.lbl_genre_qvb.setStyleSheet('''
            background-color: transparent;color: rgb(0, 0, 0);margin: 0px; padding:0px;
        ''')
        self.lbl_duration_qvb.setStyleSheet('''
            background-color: transparent; color: rgb(0, 0, 0);margin: 0px; padding:0px;
        ''')
        
        self.btn_menu.setStyleSheet('''
            background-color: transparent; color: rgb(0, 0, 0);margin: 0px; padding:0px;
        ''')

    def getMenuButton(self):
        return self.btn_menu 
    
    def crear_menu(self, action_eliminate):
        menu = QMenu()
        #menu.setStyleSheet("background-color: #b851ff; color:white; QMenu:Hover:{background-color: #f0f0f0; color:black}")
        #menu.setStyleSheet("background-color: #f0f0f0; color:white; QMenu:Hover:{background-color: #f0f0f0; color:b851ff !important;}")
        #menu.addAction("Añadir a playlist 🎶", action_add_to_playlist)
        #menu.addAction("Editar metadatos 💽", action_edit)
        menu.addAction("Quitar ✖️",action_eliminate)
        return menu

     
    def open_menu(self):
        self.btn_menu().exec_(self.btn_menu .mapToGlobal(self.btn_menu.rect().bottomLeft()))
     
    def setTitle (self, text):
        if text:
            self.lbl_title_qvb.setText(text)
        else:
            self.lbl_title_qvb.setText("Desconocido")   
            
    def setArtist (self, text):
        if text:
            self.lbl_artist_qvb.setText(text)
        else:
            self.lbl_artist_qvb.setText("Desconocido")   
        
    def setAlbum (self, text):
        if text:
            self.lbl_album_qvb.setText(text)
        else:
            self.lbl_album_qvb.setText("Desconocido")
            
    def setGenre(self, text):
        if text:
            self.lbl_genre_qvb.setText(text)
        else:
            self.lbl_genre_qvb.setText("Desconocido")
    
    def setDuration(self, text):
        if text:
            self.lbl_duration_qvb.setText(text)
        else:
            self.lbl_duration_qvb.setText("Desconocido")
            
    def setCoverImg (self, coverImage):
        if coverImage:
            # cargamos una imagen binaria
            pixmap = QPixmap()
            pixmap.loadFromData(coverImage)
            self.lbl_icon_cover_img.setPixmap(pixmap) 
        else:
            # cargamos una imagen desde el directorio
            self.lbl_icon_cover_img.setPixmap(QPixmap(COVER_IMG_DEFAULT))

        self.lbl_icon_cover_img.setMaximumSize(QtCore.QSize(60, 60))
        self.lbl_icon_cover_img.setScaledContents(True)
        
        
