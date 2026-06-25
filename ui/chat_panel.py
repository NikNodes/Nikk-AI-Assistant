from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter,QColor,QPen,QFont
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import Qt


class ChatPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.full_text = (
            "Nikk :\n\n"
            "Hello Nikunj!\n\n"
            "How can I help you?"
        )

        self.current_text = ""

        self.index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.type_text)
        self.timer.start(50)

        self.cursor_visible = True
        self.cursor_timer = QTimer()
        self.cursor_timer.timeout.connect(self.blink_cursor)
        self.cursor_timer.start(500)

        self.wave_offset = 0
        self.wave_timer = QTimer()
        self.wave_timer.timeout.connect(self.animate_waves)
        self.wave_timer.start(30)
    
    def animate_waves(self):
        self.wave_offset += 2
        self.update()

    def blink_cursor(self):
        self.cursor_visible = not self.cursor_visible
        self.update()

    def type_text(self):

        if self.index < len(self.full_text):

            self.current_text += self.full_text[self.index]

            self.index += 1

            self.update()

    def paintEvent(self,event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        painter.setPen(
            QColor(220,255,255,255)
        )

        painter.setFont(
            QFont(
                "Segoe UI",
                24,
                QFont.Weight.Bold
            )
        )

        # Water reflection lines

        painter.setPen(
            QColor(
                150,
                220,
                255,
                8
            )
        )
        for i in range(8):
            y = 90 + i*20
            painter.drawLine(
                0,
                y + (self.wave_offset+i)%20,
                self.width(),
                y + (self.wave_offset+i)%20
            )

        display_text = self.current_text

        if self.cursor_visible:
            display_text += " █"


        painter.setPen(
            QColor(
                220,
                255,
                255,
                255
            )
        )

        painter.setFont(
            QFont(
                "Segoe UI",
                18,
                QFont.Weight.Bold
            )
        )

        painter.drawText(
            40,
            40,
            self.width()-80,
            self.height()-80,
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignTop,
            display_text
        )
    