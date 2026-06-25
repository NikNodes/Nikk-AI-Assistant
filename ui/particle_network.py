from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPainter, QColor
import random
import math
from PyQt6.QtGui import QPen


class Node:
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

        self.vx = random.uniform(-0.4, 0.4)
        self.vy = random.uniform(-0.4, 0.4)


class ParticleNetwork(QWidget):

    def __init__(self):
        super().__init__()

        self.nodes = [
            Node(1600,900)
            for _ in range(150)
        ]

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):

        for node in self.nodes:

            node.x += node.vx
            node.y += node.vy

            if node.x < 0 or node.x > self.width():
                node.vx *= -1

            if node.y < 0 or node.y > self.height():
                node.vy *= -1

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        for i in range(len(self.nodes)):

            x1 = self.nodes[i].x
            y1 = self.nodes[i].y

            # Draw node

            painter.setBrush(
                QColor(
                    120,
                    220,
                    255,
                    180
                )
            )

            painter.setPen(
                QColor(
                    0,
                    0,
                    0,
                    0
                )
            )

            painter.drawEllipse(
                int(x1),
                int(y1),
                4,
                4
            )

            # Connect nearby nodes

            for j in range(i+1, len(self.nodes)):

                x2 = self.nodes[j].x
                y2 = self.nodes[j].y

                distance = math.sqrt(
                    (x2-x1)**2 +
                    (y2-y1)**2
                )

                if distance < 180:

                    alpha = int(
                        80 * (1 - distance / 180)
                    )

                    if alpha < 0:
                        alpha = 0

                    pen = QPen(
                        QColor(
                            120,
                            240,
                            255,
                            alpha
                        )
                    )

                    pen.setWidth(1)

                    painter.setPen(pen)

                    painter.drawLine(
                        int(x1),
                        int(y1),
                        int(x2),
                        int(y2)
                    )