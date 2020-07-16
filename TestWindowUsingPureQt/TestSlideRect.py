from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton

def drawRectangles() :
   for rect in listRect :
      hBox.addWidget(rect)
   print("\nRectangles dans la liste : ", len(listRect))
   print("Rectangles dans la hBox  : ", hBox.count())

def avance() :
   firstRect = listRect.pop(0)
   # hBox.removeWidget(firstRect)
   # hBox.addWidget(firstRect)
   listRect.append(firstRect)
   drawRectangles()


drag_active = False
x = 0
y = 0



app = QApplication([])
window = QWidget()

window.setGeometry(0, 0, 800, 480)	# adapted to Raspberry official display touchscreeb size
window.setWindowTitle('Test Carousel')

vBox = QVBoxLayout()
labelOrder = QLabel('Test de caroussel : essayez de faire glisser les rectangles')
labelOrder.setMaximumSize(700, 50)
labelOrder.setFont(QFont('Mosk Thin 100', 18, 60))

# Temp before detect slide / drag on rectangles
pushButton = QPushButton('avance')

vBox.addWidget(labelOrder, alignment=Qt.AlignHCenter)
vBox.addWidget(pushButton, alignment=Qt.AlignHCenter)


hBox = QHBoxLayout()

rect1 = QFrame()
rect1.setFrameShape(QFrame.Box)
rect1.setStyleSheet("background-color:red;");    # use palette instead ?

rect2 = QFrame()
rect2.setFrameShape(QFrame.Box)
rect2.setStyleSheet("background-color:green;");    # use palette instead ?

rect3 = QFrame()
rect3.setFrameShape(QFrame.Box)
rect3.setStyleSheet("background-color:blue;");    # use palette instead ?

   

listRect = []
listRect.append(rect1)
listRect.append(rect2)
listRect.append(rect3)

drawRectangles()

pushButton.clicked.connect(lambda: avance())


vBox.addLayout(hBox)

window.setLayout(vBox)

window.show()
app.exec_()
