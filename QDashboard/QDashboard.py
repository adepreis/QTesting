import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame

from DashUI import InfoRect, SpeedLabel


class MainWindow(QWidget):
    isDragActive = False

    listRect = []
    vBox = QVBoxLayout()
    hBox = QHBoxLayout()

    def __init__(self):
        super().__init__()  # inherit of QMainWindow
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt Carousel')
        self.setGeometry(0, 0, 800, 480)  # adapted to Raspberry official display touchscreen size
        self.setFixedSize(800, 480)

        self.labelSpeed = SpeedLabel(0)

        # Set window background color
        # self.setAutoFillBackground(True)
        # p = self.palette()
        # p.setColor(self.backgroundRole(), Qt.darkGray)
        # self.setPalette(p)

        self.vBox.addWidget(self.labelSpeed, alignment=Qt.AlignHCenter)

        # Hide cursor (for RPi better integration)
        self.setCursor(Qt.BlankCursor)

        rectH = self.height() - self.labelSpeed.height() - 20

        rect1 = InfoRect(200, rectH)
        rect2 = InfoRect(350, rectH)
        rect3 = InfoRect(200, rectH)

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
        self.isDragActive = True

    # override release
    def mouseReleaseEvent(self, e):
        if self.isDragActive:
            print(e.pos().x() - self.previousPos.x())
            if (e.pos().x() - self.previousPos.x()) > 15:
                self.slideFromLeft()
            elif (e.pos().x() - self.previousPos.x()) < -15:
                self.slideFromRight()

            self.isDragActive = False

    # override paint
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("background.png"))
        QWidget.paintEvent(self, event)

    def wheelEvent(self, scrollEvent):
        # modifiers = QApplication.keyboardModifiers()
        # if modifiers == Qt.ControlModifier:
        #     print("Ctrl + scroll")
        # elif modifiers == Qt.ShiftModifier:
        #     print("Shift + scroll")
        # elif modifiers == Qt.AltModifier:
        #     print("Alt + scroll")

        scrollEvent.accept()
        print("Autre scroll", scrollEvent.angleDelta().x(), " ", scrollEvent.angleDelta().y())

        if scrollEvent.angleDelta().y() > 0:
            self.slideFromRight()	# or fire event "Qt.Key_Right" ?
        elif scrollEvent.angleDelta().y() < 0:
            self.slideFromLeft()	# or fire event "Qt.Key_Left" ?

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.labelSpeed.speedUp()
        elif event.key() == Qt.Key_Down:
            self.labelSpeed.slowDown()
        elif event.key() == Qt.Key_Right:
            self.slideFromLeft()
        elif event.key() == Qt.Key_Left:
            self.slideFromRight()

        event.accept()

    def drawRectangles(self):
        for rect in self.listRect:
            self.hBox.addWidget(rect)

    def slideFromLeft(self):
        firstRect = self.listRect.pop()
        self.listRect.insert(0, firstRect)
        self.drawRectangles()

    def slideFromRight(self):
        firstRect = self.listRect.pop(0)
        self.listRect.append(firstRect)
        self.drawRectangles()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()

    # """""If implementations reset the cursor if it leaves a widget even if the mouse is grabbed.
    # If you want to have a cursor even when outside the window, call:"""""
    # app.setOverrideCursor(Qt.BlankCursor)

    window.show()
    sys.exit(app.exec_())
