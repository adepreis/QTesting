from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont, QColor, QImage, QPixmap
from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QWidget


class InfoRect(QFrame):
    def __init__(self, w, h):
        super().__init__()  # inherit of QFrame
        self.initUI()
        self.setFixedSize(w, h)

    def initUI(self):
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        # self.setLineWidth(3)
        # self.setMidLineWidth(3)
        self.setStyleSheet("background-color:rgba(240, 240, 240, 0.2); border-radius:2px;")  # use palette instead ?

        ### ADDING WIDGETS IN QFRAME (FOR TESTING PURPOSE) ###
        layout = QVBoxLayout()
        layout2 = QHBoxLayout()

        # widget = QWidget()
        # image = QImage("background.png")    # QPixmap, QImage or QIcon ? (""must be a widget"")

        # resize QPixmap : img = QPixmap("...") then img = img.scaled(w, h)

        # image.setDevicePixelRatio(2)    # 50% scale (??)
        # widget.render(image, widget.size())
        # layout2.addWidget(widget)  # QPixmap, QImage or QIcon ? (must be a widget)


        iconMusic = QLabel()    # couldnt be a QWidget() (no setPixmap method..)
        pixmap = QPixmap("music-icon.png")
        pixmap = pixmap.scaled(50, 50)
        iconMusic.setPixmap(pixmap)
        layout2.addWidget(iconMusic)


        layout2.addWidget(QLabel("Label 1"))
        layout2.addWidget(QPushButton("Test button 1"))
        layout.addLayout(layout2)

        layout.addWidget(QLabel("Label 2"))
        layout.addWidget(QPushButton("Test button 2"))

        self.setLayout(layout)
        # SOLUTION ? :
        # QApplication.focusWidget().clearFocus()
        #######################################################


class SpeedLabel(QLabel):
    MIN_SPEED = 0
    MAX_SPEED = 135

    def __init__(self, speed):
        super().__init__()  # QLabel inheriting
        self.setText(str(speed))
        self.initUI()

        self.timer = QTimer(self)
        self.timer.setInterval(1200)
        self.timer.timeout.connect(self.deceleration)

    def initUI(self):
        self.setMaximumSize(700, 75)
        self.setFont(QFont('Mosk Thin 100', 30, 60))

        palette = self.palette()
        palette.setColor(self.foregroundRole(), QColor.fromRgb(255, 255, 255, 204))  # white (80% opacity)
        self.setPalette(palette)

    def speedUp(self):
        currentSpeed = self.getSpeedValue()

        if currentSpeed < self.MAX_SPEED:
            self.setText(str(currentSpeed + 1))
            self.timer.start()  # starts deceleration phenomenon

    def slowDown(self):
        currentSpeed = self.getSpeedValue()

        if currentSpeed > self.MIN_SPEED:
            self.setText(str(currentSpeed - 1))
        else:
            self.timer.stop()  # stops deceleration phenomenon when MIN_SPEED is reached

    def getSpeedValue(self):
        return int(self.text())

    def deceleration(self):
        # simulates engine brake by decreasing speed every 1200ms
        self.slowDown()
