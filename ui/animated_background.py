from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QPainter, QColor, QLinearGradient
import random
import math

from numpy import gradient


class Particle:
    def __init__(self):

        self.x = random.randint(0, 1600)
        self.y = random.randint(0, 900)

        self.radius = random.randint(2, 8)

        self.speed = random.uniform(0.2, 1.5)

        self.alpha = random.randint(40, 150)


class AnimatedBackground(QWidget):

    def __init__(self):
        super().__init__()

        self.particles = [Particle() for _ in range(250)]
        self.wave_offset = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(16)

    def update_animation(self):

        for p in self.particles:

            p.y -= p.speed

            if p.y < 0:
                p.y = 900
        self.wave_offset += 0.03    
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        # Dark ocean color
        gradient = QLinearGradient(
            0,
            0,
            0,
            self.height()
        )

        gradient.setColorAt(
            0,
            QColor(0,15,40)
        )

        gradient.setColorAt(
            0.5,
            QColor(0,40,80)
        )

        gradient.setColorAt(
            1,
            QColor(0,10,25)
        )

        painter.fillRect(
            self.rect(),
            gradient
        )
        
        for i in range(8):

            painter.setBrush(
                QColor(
                    100,
                    200,
                    255,
                    6
                )
            )

            painter.setPen(Qt.PenStyle.NoPen)

            painter.drawEllipse(
                i * 250 - 100,
                -250,
                400,
                800
            )

            painter.setPen(
            QColor(
                100,
                220,
                255,
                30
            )
        )

        for layer in range(3):

            points = []

            amplitude = 40 + layer * 25

            y_center = (
                self.height()//2
                + layer*80
                - 80
            )

            for x in range(0, self.width(), 15):

                y = (
                    y_center
                    +
                    amplitude *
                    math.sin(
                        x*0.01
                        +
                        self.wave_offset
                        +
                        layer
                    )
                )

                points.append((x, y))

            for i in range(len(points)-1):

                painter.drawLine(
                    int(points[i][0]),
                    int(points[i][1]),
                    int(points[i+1][0]),
                    int(points[i+1][1])
                )

        for p in self.particles:

            painter.setBrush(
                QColor(
                    120,
                    220,
                    255,
                    p.alpha
                )
            )
            
            painter.drawEllipse(
                int(p.x),
                int(p.y),
                p.radius,
                p.radius
            )