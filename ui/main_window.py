from PyQt6.QtWidgets import QMainWindow
from ui import bubbles
from ui.animated_background import AnimatedBackground
from ui.orb_widget import OrbWidget
from ui.particle_network import ParticleNetwork
from ui.glass_panel import GlassPanel
from ui.bubbles import BubbleWidget
from ui.floating_gems import FloatingGems
from ui.ripple_effect import RippleEffect
from ui.title_panel import TitlePanel
from ui.status_panel import StatusPanel
from ui.chat_panel import ChatPanel
from ui.bottom_dashboard import BottomDashboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("Nikk AI Assistant")
        self.setGeometry(100,50,1600,900)

        self.background = AnimatedBackground()
        self.setCentralWidget(self.background)

        self.dashboard = BottomDashboard()

        self.dashboard.setParent(
            self.background
        )

        self.dashboard.resize(
            1200,
            100
        )

        self.dashboard.move(
            200,
            630
        )

        self.setMouseTracking(True)
        self.background.setMouseTracking(True)

        self.bubbles = BubbleWidget()
        self.bubbles.setParent(
            self.background
        )
        self.bubbles.resize(
            1600,
            900
        )

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

        self.gems = FloatingGems()
        self.gems.setParent(
            self.background
        )
        self.gems.resize(
            1600,
            900
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

        self.chat = ChatPanel()

        self.chat.setParent(
            self.panel
        )
        self.chat.resize(
            600,
            200
        )
        self.chat.move(
            20,
            20
        )
        
        self.title_panel = TitlePanel()
        self.title_panel.setParent(self.background)

        self.title_panel.resize(
            500,
            90
        )
        self.title_panel.move(
            550,
            40
        )

        self.ripple = RippleEffect()
        self.ripple.setParent(
            self.background
        )
        self.ripple.resize(
            1600,
            900
        )
    
    def mouseMoveEvent(self,event):

        self.ripple.addRipple(
            event.position().x(),
            event.position().y()
        )

        self.status_panel = StatusPanel()
        self.status_panel.setParent(self.background)

        self.status_panel.resize(
            750,
            80
        )
        self.status_panel.move(
            425,
            790
        )

        