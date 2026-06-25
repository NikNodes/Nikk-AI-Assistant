from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPainter, QColor
import random
import math


class Gem:

    def __init__(self):

        self.x = random.randint(0,1600)
        self.y = random.randint(0,900)

        self.radius = random.randint(5,10)

        self.angle = random.uniform(0,6)

        self.color = random.choice([
            QColor(255,80,120,90),
            QColor(100,255,180,90),
            QColor(180,120,255,90),
            QColor(255,220,80,90)
        ])


class FloatingGems(QWidget):

    def __init__(self):
        super().__init__()

        self.t = 0

        self.gems = [
            Gem()
            for _ in range(10)
        ]

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)


    def animate(self):

        self.t += 0.02

        self.update()


    def paintEvent(self,event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        for i,gem in enumerate(self.gems):

            yy = gem.y + 20*math.sin(self.t+i)

            painter.setPen(QColor(0,0,0,0))

            painter.setBrush(gem.color)

            painter.drawEllipse(
                int(gem.x),
                int(yy),
                gem.radius,
                gem.radius
            )