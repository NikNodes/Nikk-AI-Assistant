from PyQt6.QtWidgets import QMainWindow
from ui.animated_background import AnimatedBackground
from ui.orb_widget import OrbWidget
from ui.particle_network import ParticleNetwork
from ui.glass_panel import GlassPanel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nikk AI Assistant")
        self.setGeometry(100,50,1600,900)

        self.background = AnimatedBackground()
        self.setCentralWidget(self.background)

        self.orb = OrbWidget()

        self.orb.setParent(self.background)

        self.orb.resize(
            400,
            400
        )

        self.orb.move(
            600,
            250
        )
        self.network = ParticleNetwork()

        self.network.setParent(
            self.background
        )

        self.network.resize(
            1600,
            900
        )

        self.panel = GlassPanel()

        self.panel.setParent(
            self.background
        )

        self.panel.resize(
            650,
            230
        )

        self.panel.move(
            470,
            120
        )