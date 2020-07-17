# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Fri Jul 17 14:35:18 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(580, 492)
        main.setStyleSheet("QWidget{\n"
"    border: 0px solid grey;\n"
"    background-color: rgb(255, 131, 6);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: white;\n"
"    border: 1px solid #4495D1;\n"
"    padding: 1px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(main)
        self.verticalLayout.setSpacing(26)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(23, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 84, 16);\n"
"color: rgb(253, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtCore.Qt.ArrowCursor)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 1px solid grey;\n"
"    background-color: rgb(130, 81, 234);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #9651EA;\n"
"    border: 1px solid grey;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #AA38EA;\n"
"    border: 1px solid grey;\n"
"    color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtCore.Qt.ArrowCursor)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border: 1px solid grey;\n"
"    background-color: rgb(130, 81, 234);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #9651EA;\n"
"    border: 1px solid grey;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #AA38EA;\n"
"    border: 1px solid grey;\n"
"    color: white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        main.setWindowTitle(QtWidgets.QApplication.translate("main", "main", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("main", "Main Menu", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("main", "Текст в QR", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("main", "QR в текст", None, -1))

