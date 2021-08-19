from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, pyqtSlot, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QKeySequence, QMovie
import cv2

from main import MainWindow

class testing_mode(MainWindow):    
    def stop_cam(self):
        print("stop button pressed")
        self.logic = 0
    
    @pyqtSlot()
    def display_image(self):
        self.logic = 1
        cap = cv2.VideoCapture(0)
        
        while(cap.isOpened()):
            ret, frame = cap.read()            

            qformat = QImage.Format_Indexed8
            if len(frame.shape) == 3:
                if (frame.shape[2]) == 4:
                    qfromat = QImage.Format_RGBA888
                else:
                    qformat = QImage.Format_RGB888
            
            img = QImage(frame, frame.shape[1], frame.shape[0], qformat)
            img = img.rgbSwapped()
            if (self.logic == 1):
                self.ui.test_output.setPixmap(QPixmap.fromImage(img))
                self.ui.test_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.ui.test_error.setText("Video Working Properly")

            if (self.logic == 0):
                self.ui.test_error.setText("Video stop Properly")
                
                image6 = self.resource_path('vector/images/picupload/undraw_Taking_selfie_re_wlgd.PNG')
                self.ui.test_output.setPixmap(QPixmap(image6).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
                self.ui.test_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                
                self.empty(self.ui.test_pic)
                break            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("i am pressed at once")
                break
        cap.release()
        cv2.destroyAllWindows()
