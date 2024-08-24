import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QStackedWidget
from src.components.sidebar import Sidebar
from src.components.player_controls import PlayerControls
from src.pages.home_page import HomePage
from src.pages.playlist_page import PlaylistPage
from src.pages.credits_page import CreditsPage
from src.utils.theme_manager import ThemeManager
from src.utils.player_logic import PlayerLogic

class SpotifyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 360, 720)

        self.theme_manager = ThemeManager(QApplication.instance())

        self.player_logic = PlayerLogic()

        main_layout = QHBoxLayout()
        sidebar = Sidebar(self, theme_manager=self.theme_manager)

        self.pages = QStackedWidget()
        self.pages.addWidget(HomePage(self, self.player_logic))
        self.pages.addWidget(PlaylistPage(self, self.player_logic))
        self.pages.addWidget(CreditsPage(self))

        main_content = QWidget()
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.pages)
        content_layout.addWidget(PlayerControls(self, self.player_logic))
        main_content.setLayout(content_layout)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(main_content)
        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    def show_home_page(self):
        self.pages.setCurrentIndex(0)

    def show_playlist_page(self):
        self.pages.setCurrentIndex(1)

    def show_credits_page(self):
        self.pages.setCurrentIndex(2)

    def show_settings_page(self):
        print("Settings page not implemented yet!")

    def add_song(self):
        self.player_logic.add_song(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("assets/styles/spotify.qss")
    player = SpotifyApp()
    player.show()
    sys.exit(app.exec_())
