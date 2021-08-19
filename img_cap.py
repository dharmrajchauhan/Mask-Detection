from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, pyqtSlot, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QKeySequence, QMovie
from PyQt5.QtWidgets import QFileDialog
import cv2
import datetime

from main import MainWindow

class img_rec_mode(MainWindow):    
    def stop_cam(self):
        print("stop button pressed")
        self.logic = 0
    
    def click_cam(self):
        print("click button pressed")
        self.logic = 2
    def filesave(self):
        global filenames
        filenames = []
        filenameofuser = QFileDialog.getExistingDirectory()
        print(filenameofuser)
        print(type(filenameofuser))
        filenames.append(filenameofuser)
        self.ui.irec_error.setText(filenameofuser)
        print(f'filenames:- {filenames}')
        filename = self.ui.irec_error.text()
        return filename
    
    @pyqtSlot()
    def display_image(self):
        self.logic = 1
        self.click(self.ui.irec_pic)
        
        filename = self.ui.irec_error.text()
        # print(f'filename retrive direct:- {filename}')
        if len(filename) == 0:
            filename = img_rec_mode.filesave(self)
            print(f"call the open func and get filename is:- {filename}")
            print(str(filename[-4:]))
        elif len(filename) != 0:
            print("elif loop enter")
            print(str(filename))
            if str(filename[-4:]) == ".mp4":
                print("file extension is .mp4")
                pass
        else:
            print("file is present")
        print(f'filename pass in cap is:- {filename}')
        
        
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
                self.ui.irec_output.setPixmap(QPixmap.fromImage(img))
                self.ui.irec_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.ui.irec_error.setText("Video Working Properly")

            if (self.logic == 2):
                date =  datetime.datetime.now()
                cv2.imwrite("%s/%s%s%s_%s%s%s.jpg" %(filename, date.year, date.month, date.day, date.hour, date.minute, date.second), frame)
                self.ui.irec_error.setText("Photo click completely")
                self.click(self.ui.irec_pic)
                self.logic = 1
                
            if (self.logic == 0):
                self.ui.test_error.setText("Video stop Properly")
                self.done(self.ui.irec_pic)
                
                image5 = './vector/images/picupload/undraw_Camera_re_cnp4.PNG'
                self.ui.irec_output.setPixmap(QPixmap(image5).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
                self.ui.irec_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.empty(self.ui.irec_pic)
                break            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("i am pressed at once")
                break
        cap.release()
        cv2.destroyAllWindows()
