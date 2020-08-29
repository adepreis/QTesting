from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel

from threading import *
from Notifier import postureHelper

class SetupWindow(QWidget):
    vBox = QVBoxLayout()
    # hBox = QHBoxLayout()

    def __init__(self, width, height):
        super().__init__()
        self.initUI(width, height)

    def initUI(self, width, height):
        self.setWindowTitle('Configure SaveBack notifications')
        self.setWindowIcon(QIcon('save-back-icon.png'))
        self.setGeometry(width-300, height-300, width, height)
        self.setFixedSize(300, 300)

        self.setStyleSheet("background-color:rgba(200, 200, 200, 0.2);")
        
        global reminderInterval
        self.labelOrder = QLabel("Set reminder every " + str(reminderInterval) + " minutes :")
        self.labelOrder.setMaximumSize(width, 50)
        self.labelOrder.setMinimumSize(width, 50)
        self.labelOrder.setStyleSheet("background-color:rgba(255, 255, 255, 0.5);")
        # labelOrder.setFont(QFont('Mosk Thin 100', 20, 20))
        self.vBox.addWidget(self.labelOrder, alignment=Qt.AlignLeft)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(5)
        self.slider.setMaximum(60)
        self.slider.setValue(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        
        self.slider.setMinimumSize(width, 50)
        self.slider.setMaximumSize(width, 50)
		
        self.vBox.addWidget(self.slider, alignment=Qt.AlignHCenter)
        self.slider.valueChanged.connect(self.valuechange)
        

        # self.vBox.addLayout(self.hBox)
        
        self.setLayout(self.vBox)


    def valuechange(self):
        global reminderInterval
        reminderInterval = self.slider.value()
        self.labelOrder.setText("Set reminder every " + str(reminderInterval) + " minutes :")


    
if __name__ == '__main__':
    app = QApplication([])

    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    reminderInterval = 10
    window = SetupWindow(width, height)

    window.show()
    app.exec_()

    # The following instructions will start after closing the "app control panel"

    # TODO :
    #   - Find a way to reload timer and send notifications regularly
    #   - Multiply interval by 60 (in order to obtain a value in minutes)
    t = Timer(reminderInterval, postureHelper)
    t.start()

    postureHelper()
