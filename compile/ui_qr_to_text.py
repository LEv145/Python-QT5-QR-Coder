# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qr_to_text.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(580, 492)
        Form.setStyleSheet(u"background-color: rgb(255, 131, 6)")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 150))
        font = QFont()
        font.setFamily(u"MS Serif")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 84, 16);\n"
"color: rgb(253, 255, 255)")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 70))
        font1 = QFont()
        font1.setFamily(u"Miriam CLM")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"   border: 1px solid grey;\n"
"   background-color: rgb(130, 81, 234);\n"
"   color: white;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #9651EA;\n"
"   border: 1px solid grey;\n"
"   color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"   background-color: #AA38EA;\n"
"   border: 1px solid grey;\n"
"   color: white;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)

        self.label_2 = QTextBrowser(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: white;")

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(59, 20))
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton{\n"
"   border-radius: 5px;\n"
"   border: 1px solid grey;\n"
"   background-color: rgb(255, 46, 5);\n"
"   color: white;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:  rgb(255, 16, 5);\n"
"   border: 1px solid grey;\n"
"   color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"   background-color:  rgb(255, 0, 0);\n"
"   border: 1px solid grey;\n"
"   color: white;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"QR \u0432 \u0442\u0435\u043a\u0441\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
    # retranslateUi

