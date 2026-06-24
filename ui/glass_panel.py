from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QPainter,
    QColor,
    QPen
)


class GlassPanel(QWidget):

    def __init__(self):
        super().__init__()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        # Main body
        painter.setBrush(
            QColor(
                255,
                255,
                255,
                18
            )
        )

        painter.setPen(
            Qt.PenStyle.NoPen
        )

        painter.drawRoundedRect(
            self.rect(),
            35,
            35
        )

        # Outer border

        painter.setPen(
            QPen(
                QColor(
                    100,
                    220,
                    255,
                    130
                ),
                3
            )
        )

        painter.drawRoundedRect(
            self.rect().adjusted(
                2,
                2,
                -2,
                -2
            ),
            35,
            35
        )

        # Inner border

        painter.setPen(
            QPen(
                QColor(
                    255,
                    255,
                    255,
                    40
                ),
                1
            )
        )

        painter.drawRoundedRect(
            self.rect().adjusted(
                10,
                10,
                -10,
                -10
            ),
            30,
            30
        )

        # Reflection line

        painter.setPen(
            QPen(
                QColor(
                    255,
                    255,
                    255,
                    50
                ),
                2
            )
        )

        painter.drawLine(
            40,
            30,
            self.width()-80,
            30
        )