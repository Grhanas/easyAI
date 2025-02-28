# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 767)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.video_play_area = QLabel(self.widget)
        self.video_play_area.setObjectName(u"video_play_area")
        font = QFont()
        font.setPointSize(30)
        self.video_play_area.setFont(font)
        self.video_play_area.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.video_play_area, 0, 0, 1, 6)

        self.modal_selection_button = QPushButton(self.widget)
        self.modal_selection_button.setObjectName(u"modal_selection_button")
        font1 = QFont()
        font1.setPointSize(13)
        self.modal_selection_button.setFont(font1)

        self.gridLayout.addWidget(self.modal_selection_button, 1, 0, 1, 1)

        self.selected_modal = QLabel(self.widget)
        self.selected_modal.setObjectName(u"selected_modal")
        font2 = QFont()
        font2.setPointSize(12)
        self.selected_modal.setFont(font2)

        self.gridLayout.addWidget(self.selected_modal, 1, 1, 1, 1)

        self.select_video_button = QPushButton(self.widget)
        self.select_video_button.setObjectName(u"select_video_button")
        self.select_video_button.setFont(font1)

        self.gridLayout.addWidget(self.select_video_button, 1, 2, 1, 1)

        self.selected_video = QLabel(self.widget)
        self.selected_video.setObjectName(u"selected_video")
        self.selected_video.setFont(font2)

        self.gridLayout.addWidget(self.selected_video, 1, 3, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 1, 4, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTabletTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setInputMethodHints(Qt.ImhNone)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.label_2, 1, 5, 2, 1)

        self.use_default_model_button = QPushButton(self.widget)
        self.use_default_model_button.setObjectName(u"use_default_model_button")
        self.use_default_model_button.setFont(font1)

        self.gridLayout.addWidget(self.use_default_model_button, 2, 0, 1, 2)

        self.use_default_video_button = QPushButton(self.widget)
        self.use_default_video_button.setObjectName(u"use_default_video_button")
        self.use_default_video_button.setFont(font1)

        self.gridLayout.addWidget(self.use_default_video_button, 2, 2, 1, 2)

        self.spin_box = QSpinBox(self.widget)
        self.spin_box.setObjectName(u"spin_box")
        self.spin_box.setMaximum(1000)

        self.gridLayout.addWidget(self.spin_box, 2, 4, 1, 1)

        MainWindow.setCentralWidget(self.widget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EasyAI", None))
        self.video_play_area.setText(QCoreApplication.translate("MainWindow", u"Select Video Please !!!", None))
        self.modal_selection_button.setText(QCoreApplication.translate("MainWindow", u"Select Model", None))
        self.selected_modal.setText("")
        self.select_video_button.setText(QCoreApplication.translate("MainWindow", u"Select Video", None))
        self.selected_video.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Video speed:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"If you decrease the number, video speed will increase. You can arrange video speed according to your system requirements.", None))
        self.use_default_model_button.setText(QCoreApplication.translate("MainWindow", u"Use Default Model", None))
        self.use_default_video_button.setText(QCoreApplication.translate("MainWindow", u"Use Default Video", None))
    # retranslateUi

