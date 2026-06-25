from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPainter, QColor
import math


class Ripple:

    def __init__(self,x,y):

        self.x=x
        self.y=y

        self.radius=5
        self.alpha=120


class RippleEffect(QWidget):

    def __init__(self):

        super().__init__()

        self.ripples=[]

        self.timer=QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)


    def addRipple(self,x,y):

        self.ripples.append(
            Ripple(x,y)
        )


    def animate(self):

        for ripple in self.ripples:

            ripple.radius += 2

            ripple.alpha -= 2

        self.ripples = [
            r for r in self.ripples
            if r.alpha > 0
        ]

        self.update()


    def paintEvent(self,event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        for ripple in self.ripples:

            color = QColor(
                120,
                230,
                255,
                ripple.alpha
            )

            painter.setPen(color)

            painter.drawEllipse(
                int(ripple.x-ripple.radius),
                int(ripple.y-ripple.radius),
                ripple.radius*2,
                ripple.radius*2
            )