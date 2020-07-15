import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)
        self.pushButton.clicked.connect( self.displayAlertMsg )

    def displayAlertMsg(self) :
        QtWidgets.QMessageBox.information(self.centralwidget, "Boite de dialogue", "Coucou !")



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
