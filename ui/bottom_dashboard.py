from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import QTimer
import random


class BottomDashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.bars = [random.randint(10,80) for _ in range(30)]

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(100)

    def animate(self):

        self.bars = [
            random.randint(10,80)
            for _ in range(30)
        ]

        self.update()

    def paintEvent(self,event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        # Glass panel

        painter.setBrush(
            QColor(40,50,70,120)
        )

        painter.setPen(
            QPen(
                QColor(100,220,255,150),
                2
            )
        )

        painter.drawRoundedRect(
            self.rect(),
            25,
            25
        )

        # Audio spectrum

        x = 40

        colors = [
            QColor(0,255,255),
            QColor(255,0,255),
            QColor(255,255,0)
        ]

        for i,h in enumerate(self.bars):

            painter.setPen(
                QPen(
                    colors[i%3],
                    4
                )
            )

            painter.drawLine(
                x,
                100,
                x,
                100-h
            )

            x += 10

        painter.setPen(
            QColor(220,255,255)
        )

        painter.setFont(
            QFont(
                "Segoe UI",
                12
            )
        )

        painter.drawText(
            350,
            80,
            "STATUS : READY"
        )