# Autor: Estela Madariaga
# Fecha de creación: 2022
# Created by: PyQt5 UI code generator 5.15.4



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
from src.view.config import (APP_MAIN_WIN_WITDH, 
                         APP_MAIN_WIN_HEIGHT,LOGO_APP, 
                         MINIMIZE_ICON, 
                         NORMAL_ICON, 
                         MAXIMIZE_ICON, 
                         CLOSE_ICON,
                         BACKGROUND_COVER_IMG, 
                         BACKGROUND_COVER_IMG_SMALL, 
                         EDIT_ICON, 
                         MP3_ICON,
                         VIDEO_URL,
                         PREVIUS_ICON, 
                         PLAY_ICON, 
                         NEXT_ICON,
                         LOW_VOLUME_ICON)
class App_MainWindow(object):
        
    def setup(self, App_MainWindow):
        App_MainWindow.setObjectName("App_MainWindow")
        App_MainWindow.resize(APP_MAIN_WIN_WITDH, APP_MAIN_WIN_HEIGHT)
        App_MainWindow.setStyleSheet("QWidget{\n"
"background: transparent;\n"
"}\n"
"\n"
"QMainWindow, QWidget#centalwidget, QStatusBar{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QStatusBar{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#qfr_header {border-top: 0; border-bottom:0.5px solid #E3E3E3;}\n"
"\n"
"#qfr_footer {border-top:0.5px solid #E3E3E3; border-bottom:0;}"

)
        self.centralwidget = QtWidgets.QWidget(App_MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qfr_header = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qfr_header.sizePolicy().hasHeightForWidth())
        self.qfr_header.setSizePolicy(sizePolicy)
        self.qfr_header.setMinimumSize(QtCore.QSize(0, 70))
        self.qfr_header.setStyleSheet("")
        self.qfr_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_header.setObjectName("qfr_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.qfr_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(297, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.qfr_content_logo = QtWidgets.QFrame(self.qfr_header)
        self.qfr_content_logo.setMinimumSize(QtCore.QSize(0, 0))
        self.qfr_content_logo.setStyleSheet("")
        self.qfr_content_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_content_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_content_logo.setObjectName("qfr_content_logo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.qfr_content_logo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_logo = QtWidgets.QLabel(self.qfr_content_logo)
        self.lbl_logo.setMinimumSize(QtCore.QSize(600, 0))
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap(LOGO_APP))
        self.lbl_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_logo.setObjectName("lbl_logo")
        self.horizontalLayout.addWidget(self.lbl_logo)
        self.horizontalLayout_2.addWidget(self.qfr_content_logo)
        spacerItem1 = QtWidgets.QSpacerItem(296, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.qfr_header_content_window = QtWidgets.QFrame(self.qfr_header)
        self.qfr_header_content_window.setStyleSheet("")
        self.qfr_header_content_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_header_content_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_header_content_window.setObjectName("qfr_header_content_window")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.qfr_header_content_window)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.qfr_content_window_menu = QtWidgets.QFrame(self.qfr_header_content_window)
        self.qfr_content_window_menu.setStyleSheet("")
        self.qfr_content_window_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_content_window_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_content_window_menu.setObjectName("qfr_content_window_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.qfr_content_window_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.qfr_btns_window = QtWidgets.QHBoxLayout()
        self.qfr_btns_window.setSpacing(0)
        self.qfr_btns_window.setObjectName("qfr_btns_window")

        # Btn Minimize
        self.btn_min = QtWidgets.QPushButton(self.qfr_content_window_menu)
        self.btn_min.setStyleSheet("border:0px;")
        self.btn_min.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(MINIMIZE_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_min.setIcon(icon)
        self.btn_min.setIconSize(QtCore.QSize(25, 25))
        self.btn_min.setObjectName("btn_min")
        self.btn_min.setToolTip("minimize")
        self.qfr_btns_window.addWidget(self.btn_min)
        
         # Btn Normal 
        self.btn_rest = QtWidgets.QPushButton(self.qfr_content_window_menu)
        self.btn_rest.setStyleSheet("border:0px;")
        self.btn_rest.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(NORMAL_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rest.setIcon(icon)
        self.btn_rest.setIconSize(QtCore.QSize(20, 20))
        self.btn_rest.setObjectName("btn_rest")
        self.btn_rest.setToolTip("restore")
        self.qfr_btns_window.addWidget(self.btn_rest)
        
         # Btn Maximize
        self.btn_max = QtWidgets.QPushButton(self.qfr_content_window_menu)
        self.btn_max.setStyleSheet("border:0px;")
        self.btn_max.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(MAXIMIZE_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_max.setIcon(icon1)
        self.btn_max.setIconSize(QtCore.QSize(20, 20))
        self.btn_max.setObjectName("btn_max")
        self.btn_max.setToolTip("maximize")
        self.qfr_btns_window.addWidget(self.btn_max)

         # Btn Close
        self.btn_close = QtWidgets.QPushButton(self.qfr_content_window_menu)
        self.btn_close.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_close.setStyleSheet("border:0px;")
        self.btn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(CLOSE_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QtCore.QSize(20, 20))
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setToolTip("close")
        self.qfr_btns_window.addWidget(self.btn_close)
        self.verticalLayout_2.addLayout(self.qfr_btns_window)

        spacerItem2 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.qfr_content_window_menu, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.qfr_header_content_window)
        self.verticalLayout.addWidget(self.qfr_header, 0, QtCore.Qt.AlignTop)
        self.qfr_body = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qfr_body.sizePolicy().hasHeightForWidth())
        self.qfr_body.setSizePolicy(sizePolicy)
        self.qfr_body.setMinimumSize(QtCore.QSize(0, 600))
        self.qfr_body.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.qfr_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_body.setObjectName("qfr_body")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.qfr_body)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.qfr_body_content = QtWidgets.QHBoxLayout()
        self.qfr_body_content.setSpacing(0)
        self.qfr_body_content.setObjectName("qfr_body_content")


        #Qf left container---------------------------------------------
#         self.qfr_body_left_content = QtWidgets.QFrame(self.qfr_body)
#         #self.qfr_body_left_content.hide()
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.qfr_body_left_content.sizePolicy().hasHeightForWidth())
#         self.qfr_body_left_content.setSizePolicy(sizePolicy)
#         self.qfr_body_left_content.setMinimumSize(QtCore.QSize(350, 0))
#         self.qfr_body_left_content.setStyleSheet("background-color: rgb(0, 255, 255);")# TODO 
#         self.qfr_body_left_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.qfr_body_left_content.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.qfr_body_left_content.setObjectName("qfr_body_left_content")
#         self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.qfr_body_left_content)
#         self.verticalLayout_5.setContentsMargins(0, 0, 9, 0)
#         self.verticalLayout_5.setSpacing(0)
#         self.verticalLayout_5.setObjectName("verticalLayout_5")
#         self.qfr_display_left = QtWidgets.QFrame(self.qfr_body_left_content)
#         self.qfr_display_left.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.qfr_display_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.qfr_display_left.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.qfr_display_left.setObjectName("qfr_display_left")
#         self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.qfr_display_left)
#         self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_7.setSpacing(15)
#         self.verticalLayout_7.setObjectName("verticalLayout_7")
#         self.lbl_cover_image_zoom = QtWidgets.QLabel(self.qfr_display_left)
#         self.lbl_cover_image_zoom.setMaximumSize(QtCore.QSize(350, 350))
#         self.lbl_cover_image_zoom.setAutoFillBackground(False)
#         self.lbl_cover_image_zoom.setText("")
#         self.lbl_cover_image_zoom.setPixmap(QtGui.QPixmap(BACKGROUND_COVER_IMG))
#         self.lbl_cover_image_zoom.setScaledContents(True)
#         self.lbl_cover_image_zoom.setObjectName("lbl_cover_image_zoom")
#         self.verticalLayout_7.addWidget(self.lbl_cover_image_zoom)
#         self.qhb_playlist_plus = QtWidgets.QHBoxLayout()
#         self.qhb_playlist_plus.setContentsMargins(-1, -1, -1, 0)
#         self.qhb_playlist_plus.setSpacing(0)
#         self.qhb_playlist_plus.setObjectName("qhb_playlist_plus")
#         self.lbl_playlist = QtWidgets.QLabel(self.qfr_display_left)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_playlist.setFont(font)
#         self.lbl_playlist.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_playlist.setObjectName("lbl_playlist")
#         self.qhb_playlist_plus.addWidget(self.lbl_playlist)
#         self.btn_add_list = QtWidgets.QPushButton(self.qfr_display_left)
#         self.btn_add_list.setMinimumSize(QtCore.QSize(40, 40))
#         self.btn_add_list.setMaximumSize(QtCore.QSize(40, 40))
#         font = QtGui.QFont()
#         font.setFamily("Arial Narrow")
#         font.setPointSize(-1)
#         font.setBold(False)
#         font.setWeight(50)
#         self.btn_add_list.setFont(font)
#         self.btn_add_list.setAutoFillBackground(False)
#         self.btn_add_list.setStyleSheet("QPushButton{\n"
# "border:0px;\n"
# "color: black;\n"
# "font-size: 35px;}\n"
# "\n"
# "\n"
# "QPushButton:hover{\n"
# "border:0px;\n"
# "color:#b851ff;\n"
# "font-size: 35px;}")
#         self.btn_add_list.setIconSize(QtCore.QSize(30, 30))
#         self.btn_add_list.setObjectName("btn_add_list")
#         self.qhb_playlist_plus.addWidget(self.btn_add_list)
#         self.verticalLayout_7.addLayout(self.qhb_playlist_plus)
#         self.qlw_list_playlists = QtWidgets.QListWidget(self.qfr_display_left)
#         self.qlw_list_playlists.setStyleSheet("background-color: rgb(225, 225, 225);\n"
# "border:0px;")
#         self.qlw_list_playlists.setObjectName("qlw_list_playlists")
#         self.verticalLayout_7.addWidget(self.qlw_list_playlists)
#         self.verticalLayout_5.addWidget(self.qfr_display_left)
#         self.qfr_body_content.addWidget(self.qfr_body_left_content, 0, QtCore.Qt.AlignLeft)

        # Qf  Body ---------------------------------------------
        self.qfr_body_middle_content = QtWidgets.QFrame(self.qfr_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qfr_body_middle_content.sizePolicy().hasHeightForWidth())
        self.qfr_body_middle_content.setSizePolicy(sizePolicy)
        self.qfr_body_middle_content.setMinimumSize(QtCore.QSize(600, 0))
        # Color box centro--------------------------------------------------
        self.qfr_body_middle_content.setStyleSheet("background-color: rgb(255, 250, 255);")
        self.qfr_body_middle_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_body_middle_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_body_middle_content.setObjectName("qfr_body_middle_content")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.qfr_body_middle_content)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.qgv_video_content_middle = QVideoWidget(self.qfr_body_middle_content)
        #self.qgv_video_content_middle.hide()# TODO componente video oculto 
        self.qgv_video_content_middle.setMinimumSize(QtCore.QSize(0, 0))
        self.qgv_video_content_middle.setMaximumSize(QtCore.QSize(1677, 1677))
        self.qgv_video_content_middle.setSizeIncrement(QtCore.QSize(0, 0))
        self.qgv_video_content_middle.setStyleSheet("background-color: rgb(255, 255, 235);border:0px;") # rgb(184, 81 255) ; 
        self.qgv_video_content_middle.setObjectName("qgv_video_content_middle")
        self.verticalLayout_4.addWidget(self.qgv_video_content_middle)


        self.list_songs = QtWidgets.QListWidget(self.qfr_body_middle_content)
        self.list_songs.setMinimumSize(QtCore.QSize(0, 0))
        self.list_songs.setMaximumSize(QtCore.QSize(16777215, 300))
        self.list_songs.setSizeIncrement(QtCore.QSize(0, 0))
        self.list_songs.setAutoFillBackground(False)
        self.list_songs.setStyleSheet("background-color: rgb(234, 234, 234);border: 0px;")
        self.list_songs.setAlternatingRowColors(True)
        self.list_songs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.list_songs.setResizeMode(QtWidgets.QListView.Fixed)
        self.list_songs.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.list_songs.setViewMode(QtWidgets.QListView.ListMode)
        self.list_songs.setModelColumn(0)
        self.list_songs.setUniformItemSizes(True)
        self.list_songs.setObjectName("qlw_list_songs_middle")
        self.verticalLayout_4.addWidget(self.list_songs)
        self.qfr_body_content.addWidget(self.qfr_body_middle_content)

        
        # BOX LADO DERECHO PADRE.......................................................................
        self.qfr_body_rigth_content = QtWidgets.QFrame(self.qfr_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qfr_body_rigth_content.sizePolicy().hasHeightForWidth())
        self.qfr_body_rigth_content.setSizePolicy(sizePolicy)
        self.qfr_body_rigth_content.setMinimumSize(QtCore.QSize(350, 0))
        self.qfr_body_rigth_content.setStyleSheet("background-color: rgb(255, 255, 255);")# FLUOR
        self.qfr_body_rigth_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_body_rigth_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_body_rigth_content.setObjectName("qfr_body_rigth_content")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.qfr_body_rigth_content)
        self.verticalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
       
      

        # Crea el contenedor derecho con el formulario de los metadatos y la cover image de la cancionS
        self.contenedor_derecho = QtWidgets.QFrame(self.qfr_body_rigth_content)
        #self.contenedor_derecho.hide() # Oculto por defecto
        self.contenedor_derecho.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.contenedor_derecho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor_derecho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor_derecho.setObjectName("qfr_display_right")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.contenedor_derecho)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        # Qframe coverimage content BOX --------------------------------------------
        self.qfr_coverimage_content = QtWidgets.QFrame(self.contenedor_derecho)
        self.qfr_coverimage_content.hide()
        self.qfr_coverimage_content.setMaximumSize(QtCore.QSize(16777215, 200))
        self.qfr_coverimage_content.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.qfr_coverimage_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_coverimage_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_coverimage_content.setObjectName("qfr_coverimage_content")


        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.qfr_coverimage_content)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        # Cover image 
        self.qvb_coverimagen = QtWidgets.QVBoxLayout()
        self.qvb_coverimagen.setObjectName("qvb_coverimagen")
        spacerItem3 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.qvb_coverimagen.addItem(spacerItem3)
        self.lbl_cover_image = QtWidgets.QLabel(self.qfr_coverimage_content)
        self.lbl_cover_image.setMaximumSize(QtCore.QSize(130, 130))
        self.lbl_cover_image.setAutoFillBackground(False)
        self.lbl_cover_image.setStyleSheet("border : 1px solid #a6a6a6;")
        self.lbl_cover_image.setText("")
        self.lbl_cover_image.setPixmap(QtGui.QPixmap(BACKGROUND_COVER_IMG_SMALL))
        self.lbl_cover_image.setScaledContents(True)
        self.lbl_cover_image.setObjectName("lbl_cover_image")
        self.qvb_coverimagen.addWidget(self.lbl_cover_image, 0, QtCore.Qt.AlignHCenter)
        # Edit btn cover img
        self.btn_edit_coverimage = QtWidgets.QPushButton(self.qfr_coverimage_content)
        self.btn_edit_coverimage.setStyleSheet("QPushButton{\n"
        "border:0px;\n"
        "}\n"
        "")
        self.btn_edit_coverimage.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(EDIT_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_coverimage.setIcon(icon3)
        self.btn_edit_coverimage.setIconSize(QtCore.QSize(25, 25))
        self.btn_edit_coverimage.setObjectName("btn_edit_coverimage")
        self.btn_edit_coverimage.setToolTip("editar imagen")
        self.qvb_coverimagen.addWidget(self.btn_edit_coverimage)
        
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.qvb_coverimagen.addItem(spacerItem4)

        self.verticalLayout_11.addLayout(self.qvb_coverimagen)
        self.verticalLayout_9.addWidget(self.qfr_coverimage_content)


        self.line = QtWidgets.QFrame(self.contenedor_derecho)
        self.line.setMaximumSize(QtCore.QSize(250, 16777215))
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_9.addWidget(self.line)

        # Qframe form layout Box ----------------------------------------------------
        self.qfr_formLayout_content = QtWidgets.QFrame(self.contenedor_derecho)
        self.qfr_formLayout_content.hide()
        self.qfr_formLayout_content.setMaximumSize(QtCore.QSize(16777215, 300))
        self.qfr_formLayout_content.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.qfr_formLayout_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_formLayout_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_formLayout_content.setObjectName("qfr_formLayout_content")

        # Box interan form
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.qfr_formLayout_content)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        
        
        self.metadata_form = QtWidgets.QFormLayout()

        self.metadata_form.setContentsMargins(5, -1, 5, -1)
        self.metadata_form.setHorizontalSpacing(20)
        self.metadata_form.setVerticalSpacing(5)
        self.metadata_form.setObjectName("qfr_metadata_cotent")

        

        # lbl_metadata
        self.lbl_metadata = QtWidgets.QLabel(self.qfr_formLayout_content)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_metadata.setFont(font)
        self.lbl_metadata.setScaledContents(False)
        self.lbl_metadata.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_metadata.setObjectName("lbl_metadata")
        self.metadata_form.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.lbl_metadata)

        #title label------------------------------
        self.titleLabel = QtWidgets.QLabel(self.qfr_formLayout_content)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.titleLabel.setFont(font)
        self.titleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.metadata_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.titleLabel)

        self.titleLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.metadata_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.metadata_form.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem5)


        # artist -------------------------------------
        self.artistLabel = QtWidgets.QLabel(self.qfr_formLayout_content)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.artistLabel.setFont(font)
        self.artistLabel.setObjectName("artistLabel")
        self.metadata_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.artistLabel)

        self.artistLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.artistLineEdit.setObjectName("artistLineEdit")
        self.metadata_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.artistLineEdit)

        # Album ------------------------
        self.albumLabel = QtWidgets.QLabel(self.qfr_formLayout_content)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.albumLabel.setFont(font)
        self.albumLabel.setObjectName("albumLabel")
        self.metadata_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.albumLabel)

        self.albumLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.albumLineEdit.setObjectName("albumLineEdit")
        self.metadata_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.albumLineEdit)

        # genreLabel ------------------
        self.genreLabel = QtWidgets.QLabel(self.qfr_formLayout_content)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.genreLabel.setFont(font)
        self.genreLabel.setObjectName("genreLabel")
        self.metadata_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.genreLabel)

        self.genreLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.genreLineEdit.setObjectName("genreLineEdit")
        self.metadata_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.genreLineEdit)

        # yearLabel--------------------
        self.yearLabel = QtWidgets.QLabel(self.qfr_formLayout_content)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.yearLabel.setFont(font)
        self.yearLabel.setObjectName("yearLabel")
        self.metadata_form.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.yearLabel)

        self.yearLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.metadata_form.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.yearLineEdit)
        self.timeLabel = QtWidgets.QLabel(self.qfr_formLayout_content)

        # timelabel---------------------
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.metadata_form.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.timeLabel)

        self.timeLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.timeLineEdit.setObjectName("timeLineEdit")
        self.metadata_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.timeLineEdit)

        # trackLabel---------------
        self.trackLabel = QtWidgets.QLabel(self.qfr_formLayout_content)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.trackLabel.setFont(font)
        self.trackLabel.setObjectName("trackLabel")
        self.metadata_form.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.trackLabel)

        self.trackLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.trackLineEdit.setObjectName("trackLineEdit")
        self.metadata_form.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.trackLineEdit)

        # pathLinkLabel------------------------------
        self.pathLinkLabel = QtWidgets.QLabel(self.qfr_formLayout_content)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pathLinkLabel.setFont(font)
        
        self.pathLinkLabel.setObjectName("pathLinkLineEdit")
        self.metadata_form.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.pathLinkLabel)

        self.pathLinkLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.pathLinkLineEdit.setReadOnly(True)
        self.pathLinkLineEdit.setObjectName("pathLinkLineEdit")
        self.metadata_form.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.pathLinkLineEdit)


        spacerItem6 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.metadata_form.setItem(12, QtWidgets.QFormLayout.LabelRole, spacerItem6)
        
        

        #btn Video
        self.btn_video = QtWidgets.QPushButton(self.qfr_formLayout_content)
        self.btn_video.setStyleSheet("QPushButton{\n"
                             "border:1px dotted black;\n"
                             "padding:0px;\n"
                             "padding-left: 0px;\n"
                             "margin:0px;\n"
                             "}\n")
        self.btn_video.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(VIDEO_URL), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_video.setIcon(icon5)
        self.btn_video.setIconSize(QtCore.QSize(25, 25))
        self.btn_video.setObjectName("btn_video")
        self.btn_video.setToolTip("load video")
        self.metadata_form.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.btn_video)

        # # video Label 
        
        # self.videoLinkLabel = QtWidgets.QLabel(self.qfr_formLayout_content)
        # font = QtGui.QFont()
        # font.setFamily("Calibri")
        # font.setPointSize(12)
        # self.videoLinkLabel.setFont(font)
        # self.videoLinkLabel.setObjectName("videoLinkLabel")
        # self.metadata_form.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.videoLinkLabel)

        # video input 
        self.videoLinkLineEdit = QtWidgets.QLineEdit(self.qfr_formLayout_content)
        self.videoLinkLineEdit.setReadOnly(True)
        self.videoLinkLineEdit.setObjectName("videoLinkLineEdit")
        self.metadata_form.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.videoLinkLineEdit)
        
        self.verticalLayout_12.addLayout(self.metadata_form)
        self.verticalLayout_9.addWidget(self.qfr_formLayout_content)


        # Qframe btn save form--------------------------------------------------------- 
        self.qfr_btn_save_form = QtWidgets.QFrame(self.contenedor_derecho)
        self.qfr_btn_save_form.hide() # Oculto por defecto
        self.qfr_btn_save_form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.qfr_btn_save_form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_btn_save_form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_btn_save_form.setObjectName("qfr_btn_save_form")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.qfr_btn_save_form)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
         # Qframe btn save 
        self.btn_save = QtWidgets.QPushButton(self.qfr_btn_save_form)
        self.btn_save.setMaximumSize(QtCore.QSize(120, 35))
        # Custom Style btn save------------------------
        self.btn_save.setStyleSheet("QPushButton{\n"
        "border: 1px solid #b851ff;\n"
        #"border: 2px dotted #b851ff;\n"
        #"border-radius: 15px;\n"
        "color:#b851ff;\n"
        "font-size: 12px;}\n"
        "\n"
        "QPushButton:Hover{\n"
        "background-color: #b851ff; color:white;\n"
        "border: none;}")
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setToolTip("save metadata")
        self.horizontalLayout_8.addWidget(self.btn_save)

        # Qframe btn cancel 
        self.btn_cancel = QtWidgets.QPushButton(self.qfr_btn_save_form)
        self.btn_cancel.setMaximumSize(QtCore.QSize(120, 35))
         # Custom Style btn cancel------------------------
        self.btn_cancel.setStyleSheet("QPushButton{\n"
        "border: 1px solid #b851ff;\n"
        #"border: 2px dotted #b851ff;\n"
        #"border-radius: 15px;\n"
        "color:#b851ff;\n"
        "font-size: 12px;}\n"
        "\n"
        "QPushButton:Hover{\n"
        "background-color: #b851ff; color:white;\n"
        "border: none;}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setToolTip("cancel editing metadata")
        self.horizontalLayout_8.addWidget(self.btn_cancel)

        self.verticalLayout_9.addWidget(self.qfr_btn_save_form)
        self.verticalLayout_8.addWidget(self.contenedor_derecho)


        #----------------------------------------------------------------------------------------

        self.qfr_body_content.addWidget(self.qfr_body_rigth_content, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.qfr_body_content)
        self.verticalLayout.addWidget(self.qfr_body)
        self.qfr_footer = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qfr_footer.sizePolicy().hasHeightForWidth())
        self.qfr_footer.setSizePolicy(sizePolicy)
        self.qfr_footer.setMinimumSize(QtCore.QSize(0, 70))
        self.qfr_footer.setStyleSheet("")
        self.qfr_footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_footer.setObjectName("qfr_footer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.qfr_footer)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")


        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(20,20, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        
       

        # Qlabel Foteer 1
        self.lbl_info_song = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(30)
        self.lbl_info_song.setFixedWidth(400)
        self.lbl_info_song.setFont(font)
        self.lbl_info_song.setScaledContents(False)
        #self.lbl_info_song.setStyleSheet("border:1px solid black;")
        self.lbl_info_song.setScaledContents(False)
        self.lbl_info_song.setAlignment(QtCore.Qt.AlignLeft)
        self.lbl_info_song.setObjectName("lbl_metadata")
       
        self.horizontalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_15.addWidget(self.lbl_info_song)
        #### 

   
        self.qfr_footer_content_btns_music = QtWidgets.QFrame(self.qfr_footer)
        self.qfr_footer_content_btns_music.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.qfr_footer_content_btns_music.setMinimumSize(QtCore.QSize(0, 0))
        self.qfr_footer_content_btns_music.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qfr_footer_content_btns_music.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qfr_footer_content_btns_music.setObjectName("qfr_footer_content_btns_music")
        

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.qfr_footer_content_btns_music)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_load_song = QtWidgets.QPushButton(self.qfr_footer_content_btns_music)
        self.btn_load_song.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"")     


        self.btn_load_song.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(MP3_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_load_song.setIcon(icon4)
        self.btn_load_song.setIconSize(QtCore.QSize(40, 40))
        self.btn_load_song.setObjectName("btn_load_song")
        self.btn_load_song.setToolTip("load song")
        self.horizontalLayout_4.addWidget(self.btn_load_song)

        ### BTN MICROPHONE
        # self.btn_lyric = QtWidgets.QPushButton(self.qfr_footer_content_btns_music)
        # self.btn_lyric.setStyleSheet("QPushButton{\n"
        # "border:0px;\n"
        # "}\n"
        # "")
        # self.btn_lyric.setText("")
        # icon5 = QtGui.QIcon()
        # icon5.addPixmap(QtGui.QPixmap(LYRIC_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.btn_lyric.setIcon(icon5)
        # self.btn_lyric.setIconSize(QtCore.QSize(25, 25))
        # self.btn_lyric.setObjectName("btn_lyric")
        # self.horizontalLayout_4.addWidget(self.btn_lyric)

        self.btn_previus = QtWidgets.QPushButton(self.qfr_footer_content_btns_music)
        self.btn_previus.setStyleSheet("QPushButton{\n"
        "border:0px;\n"
        "}\n"
        "")
        self.btn_previus.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(PREVIUS_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previus.setIcon(icon6)
        self.btn_previus.setIconSize(QtCore.QSize(12, 12))
        self.btn_previus.setObjectName("btn_previus")
        self.btn_previus.setToolTip("previous song")
        self.horizontalLayout_4.addWidget(self.btn_previus)
        self.btn_play = QtWidgets.QPushButton(self.qfr_footer_content_btns_music)
        self.btn_play.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"")
        self.btn_play.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(PLAY_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon7)
        self.btn_play.setIconSize(QtCore.QSize(40, 40))
        self.btn_play.setObjectName("btn_play")
        self.btn_play.setToolTip("play")
        self.horizontalLayout_4.addWidget(self.btn_play)
        self.btn_next = QtWidgets.QPushButton(self.qfr_footer_content_btns_music)
        self.btn_next.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"")
        self.btn_next.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(NEXT_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon8)
        self.btn_next.setIconSize(QtCore.QSize(12, 12))
        self.btn_next.setObjectName("btn_next")
        self.btn_next.setToolTip("next song")
        self.horizontalLayout_4.addWidget(self.btn_next)
        self.btn_volumen = QtWidgets.QPushButton(self.qfr_footer_content_btns_music)
        self.btn_volumen.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"")
        self.btn_volumen.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(LOW_VOLUME_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_volumen.setIcon(icon9)
        self.btn_volumen.setIconSize(QtCore.QSize(25, 25))
        self.btn_volumen.setObjectName("btn_volumen")
        self.btn_next.setToolTip("volume")
        self.horizontalLayout_4.addWidget(self.btn_volumen)
        self.horizontalSlider = QtWidgets.QSlider(self.qfr_footer_content_btns_music)
        self.horizontalSlider.setStyleSheet("\n"
"QSlider{background:transparent; border-top: 0px;}\n"
"\n"
"QSlider:groove:horizontal {background:#B851FF; height: 8px; border-radius: 4px; margin: 0px} QSlider:groove:horizontal:hover {background: #6B229F}QSlider:handle:horizontal {background: black; width: 14px; height:14px; margin: -3px 0px; border-radius:7px; padding:-3px 0px;} QSlider:handle:horizontal:hover {background: black}QSlider:handle:horizontal:pressed {background:#CC94F4}\n"
"")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_4.addWidget(self.horizontalSlider)
        self.horizontalLayout_5.addWidget(self.qfr_footer_content_btns_music, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.qfr_footer, 0, QtCore.Qt.AlignBottom)
        App_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(App_MainWindow)
        self.statusbar.setObjectName("statusbar")
        App_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(App_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(App_MainWindow)


        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(0,0, 20, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_15")

        # Qlabel Footer 2 
        self.lbl_info_song_2 = QtWidgets.QLabel(self.qfr_footer)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(30)
        self.lbl_info_song_2.setFixedWidth(400)
        self.lbl_info_song_2.setFont(font)
        self.lbl_info_song_2.setScaledContents(False)
        #self.lbl_info_song_2.setStyleSheet("border:1px solid black;")
        self.lbl_info_song_2.setScaledContents(False)
        self.lbl_info_song_2.setAlignment(QtCore.Qt.AlignLeft)
        self.lbl_info_song_2.setObjectName("lbl_metadata")
       
        self.horizontalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_16.addWidget(self.lbl_info_song_2)
        



    def retranslateUi(self, App_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        App_MainWindow.setWindowTitle(_translate("App_MainWindow", "MainWindow"))
        #self.lbl_playlist.setText(_translate("App_MainWindow", "P L A Y L I S T S"))
        #self.btn_add_list.setText(_translate("App_MainWindow", "+"))
        self.lbl_metadata.setText(_translate("App_MainWindow", "METADATOS"))
        self.titleLabel.setText(_translate("App_MainWindow", "Title:"))
        self.artistLabel.setText(_translate("App_MainWindow", "Artist:"))
        self.albumLabel.setText(_translate("App_MainWindow", "Album:"))
        self.genreLabel.setText(_translate("App_MainWindow", "Genre:"))
        self.yearLabel.setText(_translate("App_MainWindow", "Year:"))
        self.timeLabel.setText(_translate("App_MainWindow", "Time:"))
        self.trackLabel.setText(_translate("App_MainWindow", "Track:"))
        self.pathLinkLabel.setText(_translate("App_MainWindow", "Path mp3:"))
        self.btn_save.setText(_translate("App_MainWindow", "Save"))
        self.btn_cancel.setText(_translate("App_MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App_MainWindow = QtWidgets.QMainWindow()
    ui = App_MainWindow()
    ui.setupUi(App_MainWindow)
    App_MainWindow.show()
    sys.exit(app.exec_())
