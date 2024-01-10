import sys
from PyQt5 import uic

from random import randint

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False
        self.circle_list = list()

        self.pushButton.clicked.connect(self.create)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setPen(QColor(255, 215, 0))
        self.circle_list.append([randint(0, 250)])
        self.circle_list[-1].append(randint(0, 399 - self.circle_list[-1][0]))
        self.circle_list[-1].append(randint(0, 561 - self.circle_list[-1][0]))

        for circle in self.circle_list:
            qp.drawEllipse(circle[1], circle[2], circle[0], circle[0])

        self.do_paint = False

    def create(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
