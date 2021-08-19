# For pyqt5 GUI--------------------------------------------------------------------------------------------
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, pyqtSlot, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QKeySequence, QMovie
from PyQt5.QtWidgets import QFileDialog
# For Mask Dection------------------------------------------------------------------------------------------
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.mobilenet import preprocess_input
import numpy as np
import cv2
from imutils import paths

# Importing Mainwindow for self------------------------------------------------------------------------------
from main import MainWindow


class video_detection(MainWindow):
    def stop_cam(self):
        print("stop button pressed")
        self.logic = 0

    def prepare(ima):
        # print("calling sucessfully")
        IMG_SIZE = 224        # image size
        img_array=ima
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE)) # resize image to match model's expected sizing
        return new_array.reshape(-1,IMG_SIZE, IMG_SIZE,3)
    
    def fileopen(self):
        global filenames
        filenames = []
        filenameofuser = QFileDialog.getOpenFileName(self, 'Please select Video file', '',"Video files (*.mp4 *.avi)")
        print(filenameofuser)
        print(type(filenameofuser))
        filenames.append(filenameofuser[0])
        self.ui.vdect_error.setText(filenameofuser[0])
        print(f'filenames:- {filenames}')
        filename = self.ui.vdect_error.text()
        return filename
    
    @pyqtSlot()
    def display_image(self):
        self.logic = 1
        # filenames = [""]
        filename = self.ui.vdect_error.text()
        # print(f'filename retrive direct:- {filename}')
        

        if len(filename) == 0:
            filename = video_detection.fileopen(self)
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
        cap = cv2.VideoCapture(filename)
        
        # Init data for detection -----------------------------------------------------------------------------------------------
        category = ["Inproper", "WithMask","WithoutMask"]
        model = tf.keras.models.load_model(self.resource_path("propinprop21.model"))
        net = cv2.dnn.readNetFromCaffe(self.resource_path('face detector/deploy.prototxt'), self.resource_path('face detector/res10_300x300_ssd_iter_140000.caffemodel'))
        
        self.record(self.ui.vdect_pic)
                
        while(cap.isOpened()):
            ret, frame = cap.read()            
            qformat = QImage.Format_Indexed8
            
            if (self.logic == 1):
                try:
                    img = frame
                    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                    hsvImg = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
                    value = 40
                    vValue = hsvImg[...,2]
                    hsvImg[...,2] = np.where((255-vValue)<value,255,vValue+value)
                    img = cv2.cvtColor(hsvImg,cv2.COLOR_HSV2RGB)
                    (h, w) = img.shape[:2]
                    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
                    net.setInput(blob)
                    detections = net.forward()
                    for i in range(0, detections.shape[2]):
                        confidence = detections[0, 0, i, 2]
                        if confidence > 0.5:
                            # print("first step pass sucessfully")
                            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                            (startX, startY, endX, endY) = box.astype("int")
                            cv2.rectangle(img, (startX,startY),(endX,endY) ,(255,0,0),2)
                            # print("rect step pass sucessfully")
                            face = img[startY:endX, startX:endX]
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                            face = cv2.resize(face, (224, 224))
                            # print("resize step pass sucessfully")
                            face = img_to_array(face)
                            face = preprocess_input(face)
                            faces = np.array(face, dtype="float32")
                            # print("faces step pass sucessfully")
                            faces = ([video_detection.prepare(faces)])
                            prediction = model.predict(faces, batch_size=32)
                            # print("model step padava pass sucessfully")
                            cla=np.argmax(prediction)
                            # print(f'cla :- {cla}')
                            score=prediction[0][cla]*100
                            op=category[np.argmax(prediction)]#+"  "+str(score)
                            if op == 'WithMask':
                                # print("withmask step pass sucessfully")
                                cv2.rectangle(img,(startX,startY),(endX,endY),(153,255,153),2)
                                cv2.putText(img,op, (startX,startY-20), cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 0, 255), 2)
                            elif op == 'WithoutMask':
                                # print("withoutmask step pass sucessfully")
                                cv2.rectangle(img,(startX,startY),(endX,endY),(0,0,255),2)
                                cv2.putText(img,op, (startX,startY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
                            elif op == 'Inproper':
                                # print("inproper step pass sucessfully")
                                cv2.rectangle(img,(startX,startY),(endX,endY),(255,0,0),2)
                                cv2.putText(img,op, (startX,startY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)
                except Exception as E:
                    self.error(self.ui.vdect_pic)
                    print(f"\n\nerror :- {E}")
                except:
                    self.error(self.ui.vdect_pic)
                    print("something gonna wrong check manually in try loop ya remove try loop you get your ans..")
                    pass
                # cv2.imshow('img',img)
                # cv2.waitKey(1)
                # if cv2.waitKey(1) & cv2.waitKey(1) == ord('q'):
                #     break
                
                # Coverting Image data to Qt5 supportad format --------------------------------------------------------------------
                try:
                    if len(frame.shape) == 3:
                        if (frame.shape[2]) == 4:
                            qfromat = QImage.Format_RGBA888
                        else:
                            qformat = QImage.Format_RGB888
                
                    simg = QImage(img, frame.shape[1], frame.shape[0], qformat)
                    simg = simg.rgbSwapped()
                except:
                    self.error(self.ui.vdect_pic)
                    print("video over bhaiya")
                    self.ui.test_error.setText("Video is over")
                    break
                
                self.ui.vdect_output.setPixmap(QPixmap.fromImage(simg))
                self.ui.vdect_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)                
                self.ui.vdect_error.setText("Detection work completely")
                
                
            if (self.logic == 0):
                self.ui.test_error.setText("Video stop Properly")
                
                image2 = self.resource_path('vector/images/videopr/undraw_Video_streaming_re_v3qg.PNG')
                self.ui.vdect_output.setPixmap(QPixmap(image2).scaled(640, 480, QtCore.Qt.KeepAspectRatio))
                self.ui.vdect_output.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
                
                self.empty(self.ui.vdect_pic)
                break            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("i am pressed at once")
                break
        cap.release()
        cv2.destroyAllWindows()
    
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        