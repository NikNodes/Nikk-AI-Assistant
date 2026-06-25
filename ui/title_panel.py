from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt


class TitlePanel(QWidget):

    def __init__(self):
        super().__init__()

        self.title = QLabel(" NIKK AI ASSISTANT", self)

        self.title.setStyleSheet("""
            color:white;
            background:transparent;
        """)

        self.title.setFont(
            QFont("Segoe UI",20,QFont.Weight.Bold)
        )

        self.title.adjustSize()
        self.title.move(120,20)

    def paintEvent(self,event):

        painter=QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # glass
        painter.setBrush(
            QColor(180,220,255,40)
        )

        painter.setPen(
            QPen(
                QColor(100,220,255,180),
                2
            )
        )

        painter.drawRoundedRect(
            self.rect(),
            35,
            35
        )

        # top shine line
        painter.setPen(
            QPen(
                QColor(255,255,255,80),
                2
            )
        )

        painter.drawLine(
            40,
            15,
            self.width()-40,
            15
        )