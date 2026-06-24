from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPainter, QColor, QPen
import math


class OrbWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.angle = 0
        self.rotation = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):
        self.angle += 0.05
        self.rotation += 2
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        cx = self.width() // 2
        cy = self.height() // 2

        # breathing effect
        radius = 80 + 10 * math.sin(self.angle)

        # glow layers
        for i in range(8):

            alpha = 25 - i * 3

            painter.setBrush(
                QColor(
                    80,
                    200,
                    255,
                    alpha
                )
            )

            painter.setPen(QColor(0, 0, 0, 0))

            painter.drawEllipse(
                int(cx-radius-i*8),
                int(cy-radius-i*8),
                int((radius+i*8)*2),
                int((radius+i*8)*2)
            )

        # center orb

        painter.setBrush(
            QColor(
                120,
                220,
                255
            )
        )

        painter.drawEllipse(
            int(cx-radius),
            int(cy-radius),
            int(radius*2),
            int(radius*2)
        )

        # Rotating rings

        painter.setBrush(QColor(0,0,0,0))
        
        painter.setPen(
        QPen(
            QColor(
                100,
                220,
                255,
                70
            ),
                3
            )
        )

        painter.drawEllipse(
            int(cx-radius-30),
            int(cy-radius-30),
            int((radius+30)*2),
            int((radius+30)*2)
        )

        painter.setPen(
            QPen(
                QColor(
                    120,
                    220,
                    255,
                    80
                ),
                2
            )
        )

        ring_radius = radius + 30

        for i in range(6):

            angle = math.radians(
                self.rotation + i*60
            )

            x = cx + ring_radius * math.cos(angle)
            y = cy + ring_radius * math.sin(angle)

            painter.drawEllipse(
                int(x)-8,
                int(y)-8,
                16,
                16
            )