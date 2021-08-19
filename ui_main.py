# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainINXTVt.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from __future__ import annotations
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt, QRect, QObject, QCoreApplication, QMetaObject, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QTabWidget, QGridLayout, QVBoxLayout, \
QHBoxLayout, QSizePolicy, QSpacerItem, QStyle, QStyleFactory, QPushButton, QFrame, QFontDialog, QStackedWidget,\
QLineEdit, QTextBrowser, QTextEdit, QPlainTextEdit, QTableWidget, QTableWidgetItem, QToolBox
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QCursor

import icons
# MainWindow.resize(950, 490)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MASK DETECTION")
        MainWindow.resize(1200, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftside_menu = QFrame(self.centralwidget)
        self.leftside_menu.setObjectName(u"leftside_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftside_menu.sizePolicy().hasHeightForWidth())
        self.leftside_menu.setSizePolicy(sizePolicy)
        self.leftside_menu.setMinimumSize(QSize(150, 0))
        self.leftside_menu.setMaximumSize(QSize(500, 16777215))
        self.leftside_menu.setSizeIncrement(QSize(0, 0))
        self.leftside_menu.setBaseSize(QSize(0, 0))
        self.leftside_menu.setStyleSheet(u"border-right: 0px;")
        self.leftside_menu.setFrameShape(QFrame.StyledPanel)
        self.leftside_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.leftside_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.leftside_menu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(149, 0))
        self.frame_6.setStyleSheet(u"border-right: 0px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 10)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: #5cb6d3;")

        self.horizontalLayout_8.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(145, 0))
        self.frame_8.setMaximumSize(QSize(500, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"border-right: 2px solid rgb(170, 255, 255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_8)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(120, 0))
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-right: 0px;\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    color: white;\n"
"}")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setGeometry(QRect(0, 0, 120, 302))
        self.page_1.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page_1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.page_1)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_17.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frame_17)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.live_detect_btn = QPushButton(self.frame_17)
        self.live_detect_btn.setObjectName(u"live_detect_btn")
        self.live_detect_btn.setStyleSheet(u"background-color: rgb(0, 79, 118);")

        self.verticalLayout_9.addWidget(self.live_detect_btn)

        self.vid_detect_btn = QPushButton(self.frame_17)
        self.vid_detect_btn.setObjectName(u"vid_detect_btn")
        self.vid_detect_btn.setStyleSheet(u"background-color: rgb(0, 79, 118);")

        self.verticalLayout_9.addWidget(self.vid_detect_btn)

        self.img_detect_btn = QPushButton(self.frame_17)
        self.img_detect_btn.setObjectName(u"img_detect_btn")
        self.img_detect_btn.setStyleSheet(u"background-color: rgb(0, 79, 118);")

        self.verticalLayout_9.addWidget(self.img_detect_btn)


        self.verticalLayout_5.addWidget(self.frame_17, 0, Qt.AlignTop)

        self.toolBox.addItem(self.page_1, u"Mask Detection")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 120, 302))
        self.verticalLayout_10 = QVBoxLayout(self.page_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.page_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setSpacing(4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.vid_rec_btn = QPushButton(self.frame_18)
        self.vid_rec_btn.setObjectName(u"vid_rec_btn")
        self.vid_rec_btn.setStyleSheet(u"background-color: rgb(0, 79, 118);")

        self.verticalLayout_13.addWidget(self.vid_rec_btn)

        self.img_rec_btn = QPushButton(self.frame_18)
        self.img_rec_btn.setObjectName(u"img_rec_btn")
        self.img_rec_btn.setStyleSheet(u"background-color: rgb(0, 79, 118);")

        self.verticalLayout_13.addWidget(self.img_rec_btn)

        self.test_rec_btn = QPushButton(self.frame_18)
        self.test_rec_btn.setObjectName(u"test_rec_btn")
        self.test_rec_btn.setStyleSheet(u"background-color: rgb(0, 79, 118);")

        self.verticalLayout_13.addWidget(self.test_rec_btn)


        self.verticalLayout_10.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.toolBox.addItem(self.page_2, u"User Data")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 120, 302))
        self.horizontalLayout_4 = QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_10)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_10)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_52)
        self.verticalLayout_29.setSpacing(4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Github = QPushButton(self.frame_52)
        self.Github.setObjectName(u"Github")
        self.Github.setStyleSheet(u"background-color: rgb(0, 79, 118);")

        self.verticalLayout_29.addWidget(self.Github)

        self.Linkedin = QPushButton(self.frame_52)
        self.Linkedin.setObjectName(u"Linkedin")
        self.Linkedin.setStyleSheet(u"background-color: rgb(0, 79, 118);")

        self.verticalLayout_29.addWidget(self.Linkedin)


        self.verticalLayout_30.addWidget(self.frame_52, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.toolBox.addItem(self.page_3, u"About")

        self.verticalLayout_3.addWidget(self.toolBox, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_8, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border-right: 0px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 15)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_9, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.leftside_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.main_container)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: #5cb6d3;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_11, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(135, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_12, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame = QFrame(self.main_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.first = QWidget()
        self.first.setObjectName(u"first")
        self.horizontalLayout_12 = QHBoxLayout(self.first)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.first)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy3.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy3)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy3.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy3)
        self.frame_20.setStyleSheet(u"border: 3px solid #437082 ")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_20)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_2.setMargin(3)

        self.verticalLayout_14.addWidget(self.label_2, 0, Qt.AlignTop)

        self.live_output = QLabel(self.frame_20)
        self.live_output.setObjectName(u"live_output")
        sizePolicy3.setHeightForWidth(self.live_output.sizePolicy().hasHeightForWidth())
        self.live_output.setSizePolicy(sizePolicy3)

        self.verticalLayout_14.addWidget(self.live_output)


        self.horizontalLayout_9.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy4)
        self.frame_19.setMinimumSize(QSize(150, 0))
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_19)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_27 = QFrame(self.frame_19)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_27)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.live_start_btn = QPushButton(self.frame_27)
        self.live_start_btn.setObjectName(u"live_start_btn")
        self.live_start_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_17.addWidget(self.live_start_btn)

        self.live_stop_btn = QPushButton(self.frame_27)
        self.live_stop_btn.setObjectName(u"live_stop_btn")
        self.live_stop_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_17.addWidget(self.live_stop_btn)


        self.verticalLayout_4.addWidget(self.frame_27)

        self.frame_34 = QFrame(self.frame_19)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(6, 0, 0, 0)
        self.live_pic = QLabel(self.frame_34)
        self.live_pic.setObjectName(u"live_pic")
        self.live_pic.setStyleSheet(u"border: 0px;")

        self.horizontalLayout_27.addWidget(self.live_pic)


        self.verticalLayout_4.addWidget(self.frame_34)


        self.horizontalLayout_9.addWidget(self.frame_19, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.live_error = QLineEdit(self.frame_15)
        self.live_error.setObjectName(u"live_error")
        self.live_error.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.live_error)


        self.verticalLayout_6.addWidget(self.frame_15, 0, Qt.AlignBottom)


        self.horizontalLayout_12.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.first)
        self.second = QWidget()
        self.second.setObjectName(u"second")
        self.horizontalLayout_16 = QHBoxLayout(self.second)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_4 = QFrame(self.second)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy3.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy3)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy3.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy3)
        self.frame_22.setStyleSheet(u"border: 3px solid #437082 ")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_22)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_22)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.label_5, 0, Qt.AlignTop)

        self.vdect_output = QLabel(self.frame_22)
        self.vdect_output.setObjectName(u"vdect_output")
        sizePolicy3.setHeightForWidth(self.vdect_output.sizePolicy().hasHeightForWidth())
        self.vdect_output.setSizePolicy(sizePolicy3)

        self.verticalLayout_15.addWidget(self.vdect_output)


        self.horizontalLayout_17.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy4.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy4)
        self.frame_23.setMinimumSize(QSize(150, 0))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_23)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_64 = QFrame(self.frame_23)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_64)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.vdect_open = QPushButton(self.frame_64)
        self.vdect_open.setObjectName(u"vdect_open")
        self.vdect_open.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.vdect_open)

        self.vdect_start_btn = QPushButton(self.frame_64)
        self.vdect_start_btn.setObjectName(u"vdect_start_btn")
        self.vdect_start_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.vdect_start_btn)

        self.vdect_stop_btn = QPushButton(self.frame_64)
        self.vdect_stop_btn.setObjectName(u"vdect_stop_btn")
        self.vdect_stop_btn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_19.addWidget(self.vdect_stop_btn)


        self.verticalLayout_8.addWidget(self.frame_64)

        self.frame_37 = QFrame(self.frame_23)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(5, 0, 0, 0)
        self.vdect_pic = QLabel(self.frame_37)
        self.vdect_pic.setObjectName(u"vdect_pic")
        self.vdect_pic.setStyleSheet(u"border: 0px;")

        self.horizontalLayout_31.addWidget(self.vdect_pic)


        self.verticalLayout_8.addWidget(self.frame_37)


        self.horizontalLayout_17.addWidget(self.frame_23, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_21)

        self.frame_24 = QFrame(self.frame_5)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.vdect_error = QLineEdit(self.frame_24)
        self.vdect_error.setObjectName(u"vdect_error")
        self.vdect_error.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.vdect_error)


        self.verticalLayout_7.addWidget(self.frame_24, 0, Qt.AlignBottom)


        self.horizontalLayout_20.addWidget(self.frame_5)


        self.horizontalLayout_16.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.second)
        self.third = QWidget()
        self.third.setObjectName(u"third")
        self.horizontalLayout_21 = QHBoxLayout(self.third)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_13 = QFrame(self.third)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_14)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy3.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy3)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy3.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy3)
        self.frame_31.setStyleSheet(u"border: 3px solid #437082 ")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_31)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_31)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_6, 0, Qt.AlignTop)

        self.idect_output = QLabel(self.frame_31)
        self.idect_output.setObjectName(u"idect_output")
        sizePolicy3.setHeightForWidth(self.idect_output.sizePolicy().hasHeightForWidth())
        self.idect_output.setSizePolicy(sizePolicy3)

        self.verticalLayout_16.addWidget(self.idect_output)


        self.horizontalLayout_26.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy4.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy4)
        self.frame_32.setMinimumSize(QSize(150, 0))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_32)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_35)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.idect_open = QPushButton(self.frame_35)
        self.idect_open.setObjectName(u"idect_open")
        self.idect_open.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.idect_open)

        self.idect_start_btn = QPushButton(self.frame_35)
        self.idect_start_btn.setObjectName(u"idect_start_btn")
        self.idect_start_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.idect_start_btn)

        self.idect_stop_btn = QPushButton(self.frame_35)
        self.idect_stop_btn.setObjectName(u"idect_stop_btn")
        self.idect_stop_btn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.idect_stop_btn)


        self.verticalLayout_12.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_32)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(5, 0, 0, 0)
        self.idec_pic = QLabel(self.frame_36)
        self.idec_pic.setObjectName(u"idec_pic")
        self.idec_pic.setStyleSheet(u"border: 0px;")

        self.horizontalLayout_30.addWidget(self.idec_pic)


        self.verticalLayout_12.addWidget(self.frame_36)


        self.horizontalLayout_26.addWidget(self.frame_32, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_30)

        self.frame_33 = QFrame(self.frame_14)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.idect_error = QLineEdit(self.frame_33)
        self.idect_error.setObjectName(u"idect_error")
        self.idect_error.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_28.addWidget(self.idect_error)


        self.verticalLayout_11.addWidget(self.frame_33, 0, Qt.AlignBottom)


        self.horizontalLayout_29.addWidget(self.frame_14)


        self.horizontalLayout_21.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.third)
        self.fourth = QWidget()
        self.fourth.setObjectName(u"fourth")
        self.horizontalLayout_10 = QHBoxLayout(self.fourth)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_25 = QFrame(self.fourth)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_26)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_26)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy3.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy3)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy3.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy3)
        self.frame_39.setStyleSheet(u"border: 3px solid #437082 ")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_39)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_39)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_21.addWidget(self.label_8, 0, Qt.AlignTop)

        self.vrec_output = QLabel(self.frame_39)
        self.vrec_output.setObjectName(u"vrec_output")
        sizePolicy3.setHeightForWidth(self.vrec_output.sizePolicy().hasHeightForWidth())
        self.vrec_output.setSizePolicy(sizePolicy3)

        self.verticalLayout_21.addWidget(self.vrec_output)


        self.horizontalLayout_32.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy4.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy4)
        self.frame_40.setMinimumSize(QSize(150, 0))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_40)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_66 = QFrame(self.frame_40)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_66)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.vrec_open = QPushButton(self.frame_66)
        self.vrec_open.setObjectName(u"vrec_open")
        self.vrec_open.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_35.addWidget(self.vrec_open)

        self.vrec_start_btn = QPushButton(self.frame_66)
        self.vrec_start_btn.setObjectName(u"vrec_start_btn")
        self.vrec_start_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_35.addWidget(self.vrec_start_btn)

        self.vrec_stop_btn = QPushButton(self.frame_66)
        self.vrec_stop_btn.setObjectName(u"vrec_stop_btn")
        self.vrec_stop_btn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_35.addWidget(self.vrec_stop_btn)


        self.verticalLayout_22.addWidget(self.frame_66)

        self.frame_65 = QFrame(self.frame_40)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(5, 0, 0, 0)
        self.vrec_pic = QLabel(self.frame_65)
        self.vrec_pic.setObjectName(u"vrec_pic")
        self.vrec_pic.setStyleSheet(u"border: 0px;")

        self.horizontalLayout_44.addWidget(self.vrec_pic)


        self.verticalLayout_22.addWidget(self.frame_65)


        self.horizontalLayout_32.addWidget(self.frame_40, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_38)

        self.frame_41 = QFrame(self.frame_26)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.vrec_error = QLineEdit(self.frame_41)
        self.vrec_error.setObjectName(u"vrec_error")
        self.vrec_error.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_33.addWidget(self.vrec_error)


        self.verticalLayout_20.addWidget(self.frame_41, 0, Qt.AlignBottom)


        self.horizontalLayout_14.addWidget(self.frame_26)


        self.horizontalLayout_10.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.fourth)
        self.fifth = QWidget()
        self.fifth.setObjectName(u"fifth")
        self.horizontalLayout_15 = QHBoxLayout(self.fifth)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_28 = QFrame(self.fifth)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_29)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_29)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy3.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy3)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy3.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy3)
        self.frame_43.setStyleSheet(u"border: 3px solid #437082 ")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_43)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_43)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_24.addWidget(self.label_9, 0, Qt.AlignTop)

        self.irec_output = QLabel(self.frame_43)
        self.irec_output.setObjectName(u"irec_output")
        sizePolicy3.setHeightForWidth(self.irec_output.sizePolicy().hasHeightForWidth())
        self.irec_output.setSizePolicy(sizePolicy3)

        self.verticalLayout_24.addWidget(self.irec_output)


        self.horizontalLayout_34.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy4.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy4)
        self.frame_44.setMinimumSize(QSize(150, 0))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_44)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_68 = QFrame(self.frame_44)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_68)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.irec_open = QPushButton(self.frame_68)
        self.irec_open.setObjectName(u"irec_open")
        self.irec_open.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_36.addWidget(self.irec_open)

        self.irec_start_btn = QPushButton(self.frame_68)
        self.irec_start_btn.setObjectName(u"irec_start_btn")
        self.irec_start_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_36.addWidget(self.irec_start_btn)

        self.irec_click_btn = QPushButton(self.frame_68)
        self.irec_click_btn.setObjectName(u"irec_click_btn")
        self.irec_click_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_36.addWidget(self.irec_click_btn)

        self.irec_stop_btn = QPushButton(self.frame_68)
        self.irec_stop_btn.setObjectName(u"irec_stop_btn")
        self.irec_stop_btn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_36.addWidget(self.irec_stop_btn)


        self.verticalLayout_25.addWidget(self.frame_68)

        self.frame_67 = QFrame(self.frame_44)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(5, 0, 0, 0)
        self.irec_pic = QLabel(self.frame_67)
        self.irec_pic.setObjectName(u"irec_pic")
        self.irec_pic.setStyleSheet(u"border: 0px;")

        self.horizontalLayout_45.addWidget(self.irec_pic)


        self.verticalLayout_25.addWidget(self.frame_67)


        self.horizontalLayout_34.addWidget(self.frame_44, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_42)

        self.frame_45 = QFrame(self.frame_29)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.irec_error = QLineEdit(self.frame_45)
        self.irec_error.setObjectName(u"irec_error")
        self.irec_error.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_35.addWidget(self.irec_error)


        self.verticalLayout_23.addWidget(self.frame_45, 0, Qt.AlignBottom)


        self.horizontalLayout_18.addWidget(self.frame_29)


        self.horizontalLayout_15.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.fifth)
        self.sixth = QWidget()
        self.sixth.setObjectName(u"sixth")
        self.horizontalLayout_22 = QHBoxLayout(self.sixth)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.sixth)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_47)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy3.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy3)
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy3.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy3)
        self.frame_49.setStyleSheet(u"border: 3px solid #437082 ")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_49)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_49)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_27.addWidget(self.label_10, 0, Qt.AlignTop)

        self.test_output = QLabel(self.frame_49)
        self.test_output.setObjectName(u"test_output")
        sizePolicy3.setHeightForWidth(self.test_output.sizePolicy().hasHeightForWidth())
        self.test_output.setSizePolicy(sizePolicy3)

        self.verticalLayout_27.addWidget(self.test_output)


        self.horizontalLayout_36.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy3.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy3)
        self.frame_50.setMinimumSize(QSize(150, 0))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_50)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_70 = QFrame(self.frame_50)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_70)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.test_start_btn = QPushButton(self.frame_70)
        self.test_start_btn.setObjectName(u"test_start_btn")
        self.test_start_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_37.addWidget(self.test_start_btn)

        self.test_stop_btn = QPushButton(self.frame_70)
        self.test_stop_btn.setObjectName(u"test_stop_btn")
        self.test_stop_btn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_37.addWidget(self.test_stop_btn)


        self.verticalLayout_28.addWidget(self.frame_70)

        self.frame_69 = QFrame(self.frame_50)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"border-left: 2px solid rgb(170, 255, 255);")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(5, 0, 0, -1)
        self.test_pic = QLabel(self.frame_69)
        self.test_pic.setObjectName(u"test_pic")
        self.test_pic.setStyleSheet(u"border: 0px;")

        self.horizontalLayout_46.addWidget(self.test_pic)


        self.verticalLayout_28.addWidget(self.frame_69)


        self.horizontalLayout_36.addWidget(self.frame_50, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_48)

        self.frame_51 = QFrame(self.frame_47)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.test_error = QLineEdit(self.frame_51)
        self.test_error.setObjectName(u"test_error")
        self.test_error.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_37.addWidget(self.test_error)


        self.verticalLayout_26.addWidget(self.frame_51, 0, Qt.AlignBottom)


        self.horizontalLayout_23.addWidget(self.frame_47)


        self.horizontalLayout_22.addWidget(self.frame_46)

        self.stackedWidget.addWidget(self.sixth)
        self.seventh = QWidget()
        self.seventh.setObjectName(u"seventh")
        self.horizontalLayout_24 = QHBoxLayout(self.seventh)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gitview = QFrame(self.seventh)
        self.gitview.setObjectName(u"gitview")
        self.gitview.setFrameShape(QFrame.StyledPanel)
        self.gitview.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.gitview)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")

        self.horizontalLayout_24.addWidget(self.gitview)

        self.stackedWidget.addWidget(self.seventh)
        self.eighth = QWidget()
        self.eighth.setObjectName(u"eighth")
        self.horizontalLayout_40 = QHBoxLayout(self.eighth)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.eighth)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_59)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_43.addWidget(self.frame_59)


        self.horizontalLayout_40.addWidget(self.frame_58)

        self.stackedWidget.addWidget(self.eighth)

        self.horizontalLayout_11.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.live_detect_btn.setText(QCoreApplication.translate("MainWindow", u"Live\n"
"Detection", None))
        self.vid_detect_btn.setText(QCoreApplication.translate("MainWindow", u"Video\n"
"Detection", None))
        self.img_detect_btn.setText(QCoreApplication.translate("MainWindow", u"Image\n"
"Detection", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), QCoreApplication.translate("MainWindow", u"Mask Detection", None))
        self.vid_rec_btn.setText(QCoreApplication.translate("MainWindow", u"Video\n"
"Recording", None))
        self.img_rec_btn.setText(QCoreApplication.translate("MainWindow", u"Image\n"
"Capture", None))
        self.test_rec_btn.setText(QCoreApplication.translate("MainWindow", u"Video\n"
"Checking", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"User Data", None))
        self.Github.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.Linkedin.setText(QCoreApplication.translate("MainWindow", u"Linked in", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"About", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VERSION: 0.21", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MASK DETECTOR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Live Mask Detection From the Webcam", None))
        self.live_output.setText("")
        self.live_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.live_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.live_pic.setText("")
        self.live_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I's good habit to close things after opening it. So after detecting, pls press stop button to shut the process.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"For Detect from Recording Video", None))
        self.vdect_output.setText("")
        self.vdect_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.vdect_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.vdect_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.vdect_pic.setText("")
        self.vdect_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I's good habit to close things after opening it. So after detecting, pls press stop button to shut the process.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"For Detect from Images", None))
        self.idect_output.setText("")
        self.idect_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.idect_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.idect_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.idec_pic.setText("")
        self.idect_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I's good habit to close things after opening it. So after detecting, pls press stop button to shut the process.", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"For Video Recording", None))
        self.vrec_output.setText("")
        self.vrec_open.setText(QCoreApplication.translate("MainWindow", u"Save Path", None))
        self.vrec_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.vrec_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.vrec_pic.setText("")
        self.vrec_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I's good habit to close things after opening it. So after recording, pls press stop button to shut the process.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"For Image Capturing", None))
        self.irec_output.setText("")
        self.irec_open.setText(QCoreApplication.translate("MainWindow", u"Save Path", None))
        self.irec_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.irec_click_btn.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.irec_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.irec_pic.setText("")
        self.irec_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I's good habit to close things after opening it. So after capturing, pls press stop button to shut the process.", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Testing Mode", None))
        self.test_output.setText("")
        self.test_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.test_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.test_pic.setText("")
        self.test_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I's good habit to close things after opening it. So after testing, pls press stop button to shut the process.", None))
    # retranslateUi























