# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qr_to_text.ui',
# licensing of 'qr_to_text.ui' applies.
#
# Created: Fri Jul 17 14:35:19 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 492)
        Form.setStyleSheet("QWidget{    \n"
"    background-color: rgb(255, 131, 6);\n"
"    border: 0px solid grey;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 0px solid #999999;\n"
"    background:  white;\n"
"    width:10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(101, 24, 255);\n"
"    min-height: 0px;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: white;\n"
"    border: 1px solid #4495D1;\n"
"    padding: 1px;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 84, 16);\n"
"color: rgb(253, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
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
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QTextBrowser(Form)
        self.label_2.setStyleSheet("QTextBrowser{\n"
"    background-color: rgb(84, 89, 99);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(59, 20))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton{\n"
"    border-radius: 10px;\n"
"    border: 1px solid grey;\n"
"    background-color: rgb(255, 46, 5);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:  rgb(255, 16, 5);\n"
"    border: 1px solid grey;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:  rgb(255, 0, 0);\n"
"    border: 1px solid grey;\n"
"    color: white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "QR в текст", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Выбрать картинку", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "Вернуться", None, -1))

