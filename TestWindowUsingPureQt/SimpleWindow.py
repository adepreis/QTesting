#import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QMessageBox


def displayAlertMsg(mainWindow) :
   QMessageBox.information(mainWindow, "Boite de dialogue", "Coucou !")

# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('Coucou !')
#     alert.exec_()

app = QApplication([])
window = QWidget() 	# should be a QMainWindow() !

window.setGeometry(0, 0, 800, 480)	# adapted to Raspberry official display touchscreen size
window.setWindowTitle('Première fenêtre PyQt5')

horizontalLayout = QHBoxLayout()

labelDescription = QLabel('Cliquer sur le bouton affiche une simple boite de dialogue.')
labelDescription.setMaximumSize(150, 100)
labelDescription.setWordWrap(True)
labelDescription.setFont(QtGui.QFont('MS UI Gothic', 12))

line = QFrame()
line.setFrameShape(QFrame.VLine)
line.setFrameShadow(QFrame.Sunken)
line.setLineWidth(2)
line.setMidLineWidth(1)

horizontalLayout.addWidget(labelDescription)
horizontalLayout.addWidget(line)

verticalLayout = QVBoxLayout()
labelOrder = QLabel('Appuyez sur le bouton suivant :')
labelOrder.setMaximumSize(500, 80)
labelOrder.setFont(QtGui.QFont('Mosk Thin 100', 20, 75))
#labelOrderFont.setBold(True)

pushButton = QPushButton('Juste ici !')
pushButton.setMinimumSize(200, 0)
pushButton.setMaximumSize(200, 50)
pushButton.setFont(QtGui.QFont('Mosk Thin 100', 22, 50))

pushButton.clicked.connect(lambda: displayAlertMsg(window))
# Or :
# pushButton.clicked.connect(on_button_clicked)

verticalLayout.addWidget(labelOrder, alignment=QtCore.Qt.AlignHCenter)
verticalLayout.addWidget(pushButton, alignment=QtCore.Qt.AlignHCenter)

horizontalLayout.addLayout(verticalLayout)

window.setLayout(horizontalLayout)

window.show()
app.exec_()
