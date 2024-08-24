from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon

class Sidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(80)
        layout = QVBoxLayout()

        home_btn = QPushButton()
        home_btn.setIcon(QIcon("assets/icons/home.svg"))
        home_btn.clicked.connect(parent.show_home_page)
        layout.addWidget(home_btn)

        playlist_btn = QPushButton()
        playlist_btn.setIcon(QIcon("assets/icons/playlist.svg"))
        playlist_btn.clicked.connect(parent.show_playlist_page)
        layout.addWidget(playlist_btn)

        settings_btn = QPushButton()
        settings_btn.setIcon(QIcon("assets/icons/settings.svg"))
        settings_btn.clicked.connect(parent.show_settings_page)
        layout.addWidget(settings_btn)

        layout.addStretch()
        self.setLayout(layout)
