# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keypad_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Keypad(object):
    def setupUi(self, Keypad):
        if not Keypad.objectName():
            Keypad.setObjectName(u"Keypad")
        Keypad.resize(302, 406)
        self.verticalLayout = QVBoxLayout(Keypad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Keypad)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.input_frame = QFrame(Keypad)
        self.input_frame.setObjectName(u"input_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.input_frame.sizePolicy().hasHeightForWidth())
        self.input_frame.setSizePolicy(sizePolicy)
        self.input_frame.setFrameShape(QFrame.NoFrame)
        self.input_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.input_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.input_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(30)
        self.lineEdit.setFont(font1)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.input_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.input_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.input_frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_4)


        self.verticalLayout.addWidget(self.input_frame)

        self.num_frame = QFrame(Keypad)
        self.num_frame.setObjectName(u"num_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.num_frame.sizePolicy().hasHeightForWidth())
        self.num_frame.setSizePolicy(sizePolicy2)
        self.num_frame.setFrameShape(QFrame.Box)
        self.num_frame.setFrameShadow(QFrame.Sunken)
        self.num_frame.setLineWidth(2)
        self.gridLayout = QGridLayout(self.num_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.zeroButton = QPushButton(self.num_frame)
        self.zeroButton.setObjectName(u"zeroButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(25)
        self.zeroButton.setFont(font2)

        self.gridLayout.addWidget(self.zeroButton, 0, 0, 1, 1)

        self.oneButton = QPushButton(self.num_frame)
        self.oneButton.setObjectName(u"oneButton")
        sizePolicy3.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy3)
        self.oneButton.setFont(font2)

        self.gridLayout.addWidget(self.oneButton, 0, 1, 1, 1)

        self.twoButton = QPushButton(self.num_frame)
        self.twoButton.setObjectName(u"twoButton")
        sizePolicy3.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy3)
        self.twoButton.setFont(font2)

        self.gridLayout.addWidget(self.twoButton, 0, 2, 1, 1)

        self.threeButton = QPushButton(self.num_frame)
        self.threeButton.setObjectName(u"threeButton")
        sizePolicy3.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy3)
        self.threeButton.setFont(font2)

        self.gridLayout.addWidget(self.threeButton, 1, 0, 1, 1)

        self.fourButton = QPushButton(self.num_frame)
        self.fourButton.setObjectName(u"fourButton")
        sizePolicy3.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy3)
        self.fourButton.setFont(font2)

        self.gridLayout.addWidget(self.fourButton, 1, 1, 1, 1)

        self.fiveButton = QPushButton(self.num_frame)
        self.fiveButton.setObjectName(u"fiveButton")
        sizePolicy3.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy3)
        self.fiveButton.setFont(font2)

        self.gridLayout.addWidget(self.fiveButton, 1, 2, 1, 1)

        self.sixButton = QPushButton(self.num_frame)
        self.sixButton.setObjectName(u"sixButton")
        sizePolicy3.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy3)
        self.sixButton.setFont(font2)

        self.gridLayout.addWidget(self.sixButton, 2, 0, 1, 1)

        self.sevenButton = QPushButton(self.num_frame)
        self.sevenButton.setObjectName(u"sevenButton")
        sizePolicy3.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy3)
        self.sevenButton.setFont(font2)

        self.gridLayout.addWidget(self.sevenButton, 2, 1, 1, 1)

        self.eightButton = QPushButton(self.num_frame)
        self.eightButton.setObjectName(u"eightButton")
        sizePolicy3.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy3)
        self.eightButton.setFont(font2)

        self.gridLayout.addWidget(self.eightButton, 2, 2, 1, 1)

        self.nineButton = QPushButton(self.num_frame)
        self.nineButton.setObjectName(u"nineButton")
        sizePolicy3.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy3)
        self.nineButton.setFont(font2)

        self.gridLayout.addWidget(self.nineButton, 3, 0, 1, 1)

        self.starButton = QPushButton(self.num_frame)
        self.starButton.setObjectName(u"starButton")
        sizePolicy3.setHeightForWidth(self.starButton.sizePolicy().hasHeightForWidth())
        self.starButton.setSizePolicy(sizePolicy3)
        self.starButton.setFont(font2)

        self.gridLayout.addWidget(self.starButton, 3, 1, 1, 1)

        self.hashButton = QPushButton(self.num_frame)
        self.hashButton.setObjectName(u"hashButton")
        sizePolicy3.setHeightForWidth(self.hashButton.sizePolicy().hasHeightForWidth())
        self.hashButton.setSizePolicy(sizePolicy3)
        self.hashButton.setFont(font2)

        self.gridLayout.addWidget(self.hashButton, 3, 2, 1, 1)


        self.verticalLayout.addWidget(self.num_frame)


        self.retranslateUi(Keypad)
        self.starButton.clicked.connect(self.lineEdit.clear)
        self.starButton.clicked.connect(self.lineEdit_2.clear)
        self.starButton.clicked.connect(self.lineEdit_3.clear)
        self.starButton.clicked.connect(self.lineEdit_4.clear)

        QMetaObject.connectSlotsByName(Keypad)
    # setupUi

    def retranslateUi(self, Keypad):
        Keypad.setWindowTitle(QCoreApplication.translate("Keypad", u"Keypad GUI", None))
        self.label.setText(QCoreApplication.translate("Keypad", u"Enter Passcode", None))
        self.zeroButton.setText(QCoreApplication.translate("Keypad", u"0", None))
        self.oneButton.setText(QCoreApplication.translate("Keypad", u"1", None))
        self.twoButton.setText(QCoreApplication.translate("Keypad", u"2", None))
        self.threeButton.setText(QCoreApplication.translate("Keypad", u"3", None))
        self.fourButton.setText(QCoreApplication.translate("Keypad", u"4", None))
        self.fiveButton.setText(QCoreApplication.translate("Keypad", u"5", None))
        self.sixButton.setText(QCoreApplication.translate("Keypad", u"6", None))
        self.sevenButton.setText(QCoreApplication.translate("Keypad", u"7", None))
        self.eightButton.setText(QCoreApplication.translate("Keypad", u"8", None))
        self.nineButton.setText(QCoreApplication.translate("Keypad", u"9", None))
        self.starButton.setText(QCoreApplication.translate("Keypad", u"*", None))
        self.hashButton.setText(QCoreApplication.translate("Keypad", u"#", None))
    # retranslateUi

