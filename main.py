# This Python file uses the following encoding: utf-8
import sys
import os
import cv2
import qrcode

from pyzbar import pyzbar

from PySide2.QtWidgets import QApplication, QWidget, QFileDialog
from PySide2.QtCore import QFile


from ui_main import Ui_main as MainWindow

from ui_text_to_qr import Ui_Form as Window1

from ui_qr_to_text import Ui_Form as Window2





class qr_to_text_windows(QWidget):
    def __init__(self):

        super(qr_to_text_windows, self).__init__()
        self.ui = Window2()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.getFileName)

        self.ui.pushButton_2.clicked.connect(self.return_window)

    def getFileName(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Выбрать файл",".", "All Files(*)")


        img = cv2.imread(filename)

        barcodes = pyzbar.decode(img)

        for barcode in barcodes:
                data = barcode.data.decode('utf-8')


        self.ui.label_2.setText(data)
        self.ui.label.setText("Текст считан")

    def return_window(self):
        self.widget = main_windows()
        self.widget.show()
        self.hide()


class text_to_qr_windows(QWidget):
    def __init__(self):
        super(text_to_qr_windows, self).__init__()

        self.path = f"{os.getcwd()}\out"

        self.ui = Window1()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.get_text)
        self.ui.pushButton_2.clicked.connect(self.return_window)
        self.ui.toolButton.clicked.connect(self.set_path)

    def get_text(self):
        text = self.ui.textEdit.toPlainText()
        img = qrcode.make(text)
        try:
            img.save(f"{self.path}\QR.png")
        except:
            os.mkdir('out')
            img.save(f"{self.path}\QR.png")
        self.ui.label.setText("Сохранено")

    def return_window(self):
        self.widget = main_windows()
        self.widget.show()
        self.hide()

    def set_path(self):
        dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
        self.path = dirlist



class main_windows(QWidget):
    def __init__(self, parent=None):
        super(main_windows, self).__init__(parent)
        self.ui = MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.to_window1)
        self.ui.pushButton_2.clicked.connect(self.to_window2)


        #self.load_ui()


    def to_window1(self):
        self.widget = text_to_qr_windows()
        self.widget.show()
        self.hide()

    def to_window2(self):
        self.widget = qr_to_text_windows()
        self.widget.show()
        self.hide()



#    def load_ui(self):
#        loader = QUiLoader()
#        path = os.path.join(os.path.dirname(__file__), "main.ui")
#        ui_file = QFile(path)
#        ui_file.open(QFile.ReadOnly)
#        loader.load(ui_file, self)
#        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = main_windows()
    widget.show()

    sys.exit(app.exec_())
