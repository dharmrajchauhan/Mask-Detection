'''
    Check "Story.py" file..
'''

from __future__ import print_function
import os
import sys
# from PyQt5.uic import loadUi
# from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QRect, QObject, QCoreApplication, QMetaObject, QPropertyAnimation, QTimer, pyqtSlot, QThread, \
pyqtSignal, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QTabWidget, QGridLayout, QVBoxLayout, \
QHBoxLayout, QSizePolicy, QSpacerItem, QStyle, QStyleFactory, QPushButton, QFrame, QFontDialog, QStackedWidget, \
QMainWindow, QMessageBox, QTableWidget, QGraphicsDropShadowEffect, QSystemTrayIcon, QMenu, qApp, QToolBox
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QKeySequence, QMovie
from PyQt5.QtWebEngineWidgets import QWebEngineView
import datetime
import signal
import cv2
import random

from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    # =============================================================================
    #     initilize a mainwindow as self
    # =============================================================================
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.logic = 0
        self.setWindowIcon(QIcon(self.resource_path('image/profile.ico')))
        self.setWindowIcon(QIcon(self.resource_path('image/syringe (3).ico')))
        
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
        # set first page as a live mask detection page ----------------------------------------------------------------
        # change as your need --
        self.ui.toolBox.setCurrentIndex(0)
        # print(self.ui.toolBox.currentIndex())
        if int(self.ui.toolBox.currentIndex()) == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.first)
        
    # Connect left side menu with Qwidget pages --------------------------------------------------------------------
        self.ui.live_detect_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.first))
        self.ui.live_detect_btn.clicked.connect(lambda: self.start(self.ui.live_pic))
        
        self.ui.vid_detect_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.second))
        self.ui.vid_detect_btn.clicked.connect(lambda: self.start(self.ui.vdect_pic))
        
        self.ui.img_detect_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.third))
        self.ui.img_detect_btn.clicked.connect(lambda: self.start(self.ui.idec_pic))
        
        self.ui.vid_rec_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fourth))
        self.ui.vid_rec_btn.clicked.connect(lambda: self.start(self.ui.vrec_pic))
        
        self.ui.img_rec_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fifth))
        self.ui.img_rec_btn.clicked.connect(lambda: self.start(self.ui.irec_pic))
        
        self.ui.test_rec_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sixth))
        self.ui.test_rec_btn.clicked.connect(lambda: self.start(self.ui.test_pic))
        
        self.ui.Github.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.seventh))
        self.ui.Github.clicked.connect(lambda: self.github())
    # Base Image set --------------------------------------------------------------
        image1 = self.resource_path('vector/images/serching/undraw_Location_search_re_ttoj.PNG')
        image2 = self.resource_path('vector/images/videopr/undraw_Video_streaming_re_v3qg.PNG')
        image3 = self.resource_path('vector/images/picupload/undraw_content_team_3epn.PNG')
        image4 = self.resource_path('vector/images/picupload/undraw_Live_photo_re_4khn.PNG')
        image5 = self.resource_path('vector/images/picupload/undraw_Camera_re_cnp4.PNG')
        image6 = self.resource_path('vector/images/picupload/undraw_Taking_selfie_re_wlgd.PNG')
        
        self.ui.live_output.setPixmap(QPixmap(image1).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
        self.ui.live_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.ui.vdect_output.setPixmap(QPixmap(image2).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
        self.ui.vdect_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
        self.ui.idect_output.setPixmap(QPixmap(image3).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
        self.ui.idect_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
        self.ui.vrec_output.setPixmap(QPixmap(image4).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
        self.ui.vrec_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
        self.ui.irec_output.setPixmap(QPixmap(image5).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
        self.ui.irec_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
        self.ui.test_output.setPixmap(QPixmap(image6).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
        self.ui.test_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
        
    # mask detection---------------------------------------------------------------
        from live_dect import live_detection
        self.ui.live_start_btn.clicked.connect(lambda: live_detection.display_image(self))
        self.ui.live_stop_btn.clicked.connect(lambda: live_detection.stop_cam(self))
        
        from vid_dect import video_detection
        self.ui.vdect_start_btn.clicked.connect(lambda: video_detection.display_image(self))
        self.ui.vdect_stop_btn.clicked.connect(lambda: video_detection.stop_cam(self))
        self.ui.vdect_open.clicked.connect(lambda: video_detection.fileopen(self))
        
        from img_dect import image_detection
        self.ui.idect_start_btn.clicked.connect(lambda: image_detection.display_image(self))
        self.ui.idect_stop_btn.clicked.connect(lambda: image_detection.stop_cam(self))
        self.ui.idect_open.clicked.connect(lambda: image_detection.fileopen(self))
        
        
    # recrording ------------------------------------------------------------------
        from video_rec import vid_rec_mode
        self.ui.vrec_start_btn.clicked.connect(lambda: vid_rec_mode.video_recording(self))
        self.ui.vrec_stop_btn.clicked.connect(lambda: vid_rec_mode.stop_cam(self))
        self.ui.vrec_open.clicked.connect(lambda: vid_rec_mode.filesave(self))
        
        from img_cap import img_rec_mode
        self.ui.irec_start_btn.clicked.connect(lambda: img_rec_mode.display_image(self))
        self.ui.irec_stop_btn.clicked.connect(lambda: img_rec_mode.stop_cam(self))
        self.ui.irec_click_btn.clicked.connect(lambda: img_rec_mode.click_cam(self))
        self.ui.irec_open.clicked.connect(lambda: img_rec_mode.filesave(self))
        
        # video testing ---------------------------------------------------------------
        
        from test_rec import testing_mode    
        self.ui.test_start_btn.clicked.connect(lambda: testing_mode.display_image(self))
        self.ui.test_stop_btn.clicked.connect(lambda: testing_mode.stop_cam(self))
        
        
        
    # #--------------------------------------------------------------------------------
    #     print(self.ui.stackedWidget.currentIndex())
    def empty(self, x):
        gif = QMovie("n")
        gif.setScaledSize(QSize().scaled(200, 300, QtCore.Qt.KeepAspectRatio))
        x.setMovie(gif)
        gif.start()
        
    def start(self, x):
        image1 = self.resource_path('vector/gif/ezgif.com-gif-maker (1).gif')
        image2 = self.resource_path('vector/gif/ezgif.com-gif-maker (2).gif')
        image3 = self.resource_path('vector/gif/ezgif.com-gif-maker (4).gif')
        image4 = self.resource_path('vector/gif/ezgif.com-gif-maker (5).gif')
        image5 = self.resource_path('vector/gif/ezgif.com-gif-maker (6).gif')
        
        mylist = [image1,image2,image3,image4,image5]
        print((random.sample(mylist, k=1)))
        m = random.sample(mylist, k=1)
        n = m[0]
        
        gif = QMovie(n)
        gif.setScaledSize(QSize().scaled(200, 300, QtCore.Qt.KeepAspectRatio))
        x.setMovie(gif)
        gif.start()
        
    def error(self, x):
        image1 = self.resource_path('vector/gif/ezgif.com-gif-maker (8).gif')
        image2 = self.resource_path('vector/gif/ezgif.com-gif-maker (9).gif')
        image3 = self.resource_path('vector/gif/ezgif.com-gif-maker (11).gif')
        image4 = self.resource_path('vector/gif/ezgif.com-gif-maker (7).gif')
        
        mylist = [image1,image2,image3,image4]
        print((random.sample(mylist, k=1)))
        m = random.sample(mylist, k=1)
        n = m[0]
        
        gif = QMovie(n)
        gif.setScaledSize(QSize().scaled(200, 300, QtCore.Qt.KeepAspectRatio))
        x.setMovie(gif)
        gif.start()
    
    def click(self, x):
        image1 = self.resource_path('vector/gif/ezgif.com-gif-maker (14).gif')
        image2 = self.resource_path('vector/gif/ezgif.com-gif-maker (15).gif')
        image3 = self.resource_path('vector/gif/ezgif.com-gif-maker (16).gif')
        image4 = self.resource_path('vector/gif/ezgif.com-gif-maker (17).gif')
        
        mylist = [image1,image2,image3,image4]
        print((random.sample(mylist, k=1)))
        m = random.sample(mylist, k=1)
        n = m[0]
        
        gif = QMovie(n)
        gif.setScaledSize(QSize().scaled(200, 300, QtCore.Qt.KeepAspectRatio))
        x.setMovie(gif)
        gif.start()
    
    def search(self, x):
        
        image1 = self.resource_path('vector/gif/ezgif.com-gif-maker (12).gif')
        image2 = self.resource_path('vector/gif/ezgif.com-gif-maker (13).gif')        
        
        mylist = [image1,image2]
        print((random.sample(mylist, k=1)))
        m = random.sample(mylist, k=1)
        n = m[0]
        
        gif = QMovie(n)
        gif.setScaledSize(QSize().scaled(200, 300, QtCore.Qt.KeepAspectRatio))
        x.setMovie(gif)
        gif.start()
        
    def record(self, x):
        
        image1 = self.resource_path('vector/gif/ezgif.com-gif-maker (14).gif')
        image2 = self.resource_path('vector/gif/ezgif.com-gif-maker (15).gif')
        image3 = self.resource_path('vector/gif/ezgif.com-gif-maker (16).gif')
        
        mylist = [image1,image2,image3]
        print((random.sample(mylist, k=1)))
        m = random.sample(mylist, k=1)
        n = m[0]
        
        gif = QMovie(n)
        gif.setScaledSize(QSize().scaled(200, 300, QtCore.Qt.KeepAspectRatio))
        x.setMovie(gif)
        gif.start()
    
    def done(self, x):
        
        image1 = self.resource_path('vector/gif/ezgif.com-gif-maker (17).gif')
        image2 = self.resource_path('vector/gif/ezgif.com-gif-maker (18).gif')
        image3 = self.resource_path('vector/gif/ezgif.com-gif-maker (19).gif')
        image4 = self.resource_path('vector/gif/ezgif.com-gif-maker (7).gif')
        
        mylist = [image1,image2,image3,image4]
        print((random.sample(mylist, k=1)))
        m = random.sample(mylist, k=1)
        n = m[0]
        
        gif = QMovie(n)
        gif.setScaledSize(QSize().scaled(200, 300, QtCore.Qt.KeepAspectRatio))
        x.setMovie(gif)
        gif.start()
        
    def shutprocess(self):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                self.close()
            except:
                sys.exit()
            print('Window closed')
        else:
            pass
    
    def resource_path(self, path):
        frozen = 'not'
        if getattr(sys, 'frozen', False):
                # we are running in executable mode
                frozen = 'ever so'
                app_dir = sys._MEIPASS
        else:
                # we are running in a normal Python environment
                app_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(app_dir, path)
    
    @pyqtSlot()
    def github(self):
        web = QWebEngineView(self.ui.gitview)
        web.setUrl(QUrl("https://github.com/Ubtohts/Mask-Detection"))
        web.resize(950, 700)
        web.show()

def sigint_handler(*args):
    """Handler for the SIGINT signal."""
    sys.stderr.write('\r')
    if QMessageBox.question(None, '', "Are you sure you want to quit?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No) == QMessageBox.Yes:
        QApplication.quit()
            # qApp.quit()
    

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    app = QApplication(sys.argv)
    window = MainWindow()
    timer = QTimer()
    timer.start(500)  # You may change this if you wish.
    timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.
    window.show()
    
    sys.exit(app.exec_())