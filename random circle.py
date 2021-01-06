import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QImage
from random import randint
import random

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 500)
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.image.fill(QColor(255, 255, 255))
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(60, 60)
        self.btn.clicked.connect(self.click)
        self.show()

    def paintEvent(self, e):
        paint = QPainter(self)
        paint.drawImage(0, 0, self.image)

    def click(self):
        r = lambda: random.randint(0, 255)

        self.paint = QPainter(self.image)
        x, y = [randint(10, 400) for j in range(2)]
        w = randint(10, 100)
        self.paint.setBrush(QColor('#%02X%02X%02X' % (r(), r(), r())))
        self.paint.drawEllipse(x, y, w, w)
        self.update()
        r = lambda: random.randint(0, 255)

        self.paint = QPainter(self.image)
        x, y = [randint(10, 400) for j in range(2)]
        w = randint(10, 100)
        self.paint.setBrush(QColor('#%02X%02X%02X' % (r(), r(), r())))
        self.paint.drawEllipse(x, y, w, w)


app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())
