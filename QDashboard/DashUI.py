# from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QFrame, QLabel


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


class SpeedLabel(QLabel):
    MIN_SPEED = 0
    MAX_SPEED = 135

    def __init__(self, speed):
        super().__init__()  # QLabel inheriting
        self.setText(str(speed))
        self.initUI()

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

    def slowDown(self):
        currentSpeed = self.getSpeedValue()

        if currentSpeed > self.MIN_SPEED:
            self.setText(str(currentSpeed - 1))

    def getSpeedValue(self):
        return int(self.text())
