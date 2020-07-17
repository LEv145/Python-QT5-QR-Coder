# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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


class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(580, 492)
        main.setStyleSheet(u"background-color: rgb(255, 131, 6)")
        self.verticalLayout = QVBoxLayout(main)
        self.verticalLayout.setSpacing(26)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalSpacer = QSpacerItem(23, 14, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(main)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 150))
        font = QFont()
        font.setFamily(u"MS Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 84, 16);\n"
"color: rgb(253, 255, 255)")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.pushButton = QPushButton(main)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 70))
        font1 = QFont()
        font1.setFamily(u"Sitka Small")
        font1.setPointSize(11)
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

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(main)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 70))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.label.setText(QCoreApplication.translate("main", u"Main Menu", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"QR \u0432 \u0442\u0435\u043a\u0441\u0442", None))
        self.pushButton_2.setText(QCoreApplication.translate("main", u"\u0422\u0435\u043a\u0441\u0442 \u0432 QR", None))
    # retranslateUi

