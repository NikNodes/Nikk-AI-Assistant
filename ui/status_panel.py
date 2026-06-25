from PyQt6.QtWidgets import QWidget,QLabel
from PyQt6.QtGui import QPainter,QColor,QPen,QFont


class StatusPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.label=QLabel("STATUS : READY",self)

        self.label.setFont(
            QFont("Segoe UI",18,QFont.Weight.Bold)
        )

        self.label.setStyleSheet("""
            color:white;
            background:transparent;
        """)

        self.label.adjustSize()
        self.label.move(200,20)

    def paintEvent(self,event):

        painter=QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        painter.setBrush(
            QColor(180,220,255,30)
        )

        painter.setPen(
            QPen(
                QColor(100,220,255,160),
                2
            )
        )

        painter.drawRoundedRect(
            self.rect(),
            25,
            25
        )