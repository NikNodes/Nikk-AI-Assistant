from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPainter, QColor
import random


class Bubble:
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

        self.radius = random.randint(2, 8)

        self.speed = random.uniform(0.3, 1.2)

        self.alpha = random.randint(20, 80)


class BubbleWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.bubbles = [
            Bubble(1600, 900)
            for _ in range(80)
        ]

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):

        for bubble in self.bubbles:

            bubble.y -= bubble.speed

            if bubble.y < -20:

                bubble.y = self.height()+20
                bubble.x = random.randint(0, self.width())

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        for bubble in self.bubbles:

            painter.setPen(
                QColor(
                    180,
                    240,
                    255,
                    bubble.alpha
                )
            )

            painter.setBrush(
                QColor(
                    180,
                    240,
                    255,
                    15
                )
            )

            painter.drawEllipse(
                int(bubble.x),
                int(bubble.y),
                bubble.radius,
                bubble.radius
            )