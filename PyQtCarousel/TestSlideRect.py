from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame



class MainWindow(QWidget):
    _drag_active = False
    
    listRect = []
    vBox = QVBoxLayout()
    hBox = QHBoxLayout()

    def __init__(self):
        super().__init__()    # inherit of QWidget
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt Carousel')
        self.setGeometry(0, 0, 800, 480)	# adapted to Raspberry official display touchscreen size
        self.setFixedSize(800, 480)

        labelOrder = QLabel('Caroussel : faites glisser les rectangles')
        labelOrder.setMaximumSize(700, 50)
        labelOrder.setFont(QFont('Mosk Thin 100', 18, 60))

        self.vBox.addWidget(labelOrder, alignment=Qt.AlignHCenter)


        rect1 = QFrame()
        rect1.setFrameShape(QFrame.Box)
        rect1.setStyleSheet("background-color:red;");        # use palette instead ?

        rect2 = QFrame()
        rect2.setFrameShape(QFrame.Box)
        rect2.setStyleSheet("background-color:green;");     # use palette instead ?

        rect3 = QFrame()
        rect3.setFrameShape(QFrame.Box)
        rect3.setStyleSheet("background-color:blue;");      # use palette instead ?

        self.listRect.append(rect1)
        self.listRect.append(rect2)
        self.listRect.append(rect3)

        self.drawRectangles()

        self.vBox.addLayout(self.hBox)
        self.setLayout(self.vBox)

    # override click
    def mousePressEvent(self, e):
        self.previousPos = e.pos()

    # override move
    def mouseMoveEvent(self, e):
        # self.previousPos = e.pos()
        self._drag_active = True

    # override release
    def mouseReleaseEvent(self, e):
        if self._drag_active:
            print(e.pos().x() - self.previousPos.x())
            if (e.pos().x() - self.previousPos.x()) > 5:
                self.slideFromLeft()
            elif (e.pos().x() - self.previousPos.x()) < -5:
                self.slideFromRight()
                
            self._drag_active = False
 

    def drawRectangles(self) :
        for rect in self.listRect :
            self.hBox.addWidget(rect)

    def slideFromLeft(self) :
        firstRect = self.listRect.pop()
        # hBox.removeWidget(firstRect)
        # hBox.addWidget(firstRect)
        self.listRect.insert(0, firstRect)
        self.drawRectangles()
        
    def slideFromRight(self) :
        firstRect = self.listRect.pop(0)
        # hBox.removeWidget(firstRect)
        # hBox.addWidget(firstRect)
        self.listRect.append(firstRect)
        self.drawRectangles()



app = QApplication([])
window = MainWindow()

window.show()
app.exec_()
