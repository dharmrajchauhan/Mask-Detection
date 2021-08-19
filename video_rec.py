from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, pyqtSlot, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QKeySequence, QMovie
from PyQt5.QtWidgets import QFileDialog
import cv2
from main import MainWindow

class vid_rec_mode(MainWindow):
    
    def stop_cam(self):
        print("stop button pressed")
        self.logic = 0
    
    def filesave(self):
        global filenames
        filenames = []
        filenameofuser = QFileDialog.getSaveFileName(self, 'Please select File SavePath', '',"Video files (*.mp4)")
        print(filenameofuser)
        print(type(filenameofuser))
        filenames.append(filenameofuser[0])
        self.ui.vrec_error.setText(filenameofuser[0])
        print(f'filenames:- {filenames}')
        filename = self.ui.vrec_error.text()
        return filename

    @pyqtSlot()
    def video_recording(self):
        self.logic = 1
        self.record(self.ui.vrec_pic)
        
        image1 = self.resource_path('vector/gif/ezgif.com-gif-maker (1).gif')
        gif = QMovie(image1)
        gif.setScaledSize(QSize().scaled(200, 300, QtCore.Qt.KeepAspectRatio))
        self.ui.vrec_pic.setMovie(gif)
        gif.start()
        
        filename = self.ui.vrec_error.text()
        # print(f'filename retrive direct:- {filename}')
        if len(filename) == 0:
            filename = vid_rec_mode.filesave(self)
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
        output_video = cv2.VideoWriter(filename , 1, 30.0, (640,480))
        # output_video = cv2.VideoWriter("{filename}/%s%s%s_%s%s%s.mp4" %(date.year, date.month, date.day, date.hour, date.minute, date.second), 1, 30.0, (640,480))
        print("file has been created")
        
        def display_video(self, frame, window=1):
            qformat = QImage.Format_Indexed8
            if len(frame.shape) == 3:
                if (frame.shape[2]) == 4:
                    qfromat = QImage.Format_RGBA888
                else:
                    qformat = QImage.Format_RGB888
            
            img = QImage(frame, frame.shape[1], frame.shape[0], qformat)
            img = img.rgbSwapped()
            self.ui.vrec_output.setPixmap(QPixmap.fromImage(img))
            self.ui.vrec_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.ui.vrec_error.setText("Start video recording.. ")
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            
            if ret == True:
                # print(f"pass frame {frame.shape}")
                display_video(self, frame, 1)
                cv2.waitKey()
                
                if (self.logic == 1):
                    # print("writing start buddy")
                    output_video.write(frame)
                
                if (self.logic == 0):
                    print(" i am break th loop")
                    self.ui.vrec_error.setText("Stopped video recording.. ")
                    self.done(self.ui.vrec_pic)
                    
                    image4 = self.resource_path('vector/images/picupload/undraw_Live_photo_re_4khn.PNG')
                    self.ui.vrec_output.setPixmap(QPixmap(image4).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
                    self.ui.vrec_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
                    self.empty(self.ui.vrec_pic)
                    break
            else:
                print("something gonna be a wrong happen here")
            
        cap.release()
        cv2.destroyAllWindows()