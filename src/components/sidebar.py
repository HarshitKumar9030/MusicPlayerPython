from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon

class Sidebar(QWidget):
    def __init__(self, parent=None, theme_manager=None):
        super().__init__(parent)
        self.setFixedWidth(80)
        layout = QVBoxLayout()

        home_btn = QPushButton()
        home_btn.setIcon(QIcon("assets/icons/home.svg"))
        home_btn.setToolTip("Home")
        home_btn.clicked.connect(parent.show_home_page)
        layout.addWidget(home_btn)

        playlist_btn = QPushButton()
        playlist_btn.setIcon(QIcon("assets/icons/playlist.svg"))
        playlist_btn.setToolTip("Playlists")
        playlist_btn.clicked.connect(parent.show_playlist_page)
        layout.addWidget(playlist_btn)

        credits_btn = QPushButton()
        credits_btn.setIcon(QIcon("assets/icons/author.svg"))
        credits_btn.setToolTip("Credits")
        credits_btn.clicked.connect(parent.show_credits_page)
        layout.addWidget(credits_btn)

        settings_btn = QPushButton()
        settings_btn.setIcon(QIcon("assets/icons/settings.svg"))
        settings_btn.setToolTip("Settings")
        settings_btn.clicked.connect(parent.show_settings_page)
        layout.addWidget(settings_btn)

        self.theme_manager = theme_manager
        self.theme_switcher_btn = QPushButton()
        self.update_theme_icon()
        self.theme_switcher_btn.setToolTip("Toggle Theme")
        self.theme_switcher_btn.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_switcher_btn)

        layout.addStretch()
        self.setLayout(layout)

    def update_theme_icon(self):
        """Update the theme icon based on the current mode."""
        if self.theme_manager.is_dark_mode:
            self.theme_switcher_btn.setIcon(QIcon("assets/icons/moon.svg"))
        else:
            self.theme_switcher_btn.setIcon(QIcon("assets/icons/sun.svg"))

    def toggle_theme(self):
        """Toggle between dark and light themes."""
        self.theme_manager.toggle_theme()
        self.update_theme_icon()
