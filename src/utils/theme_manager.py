from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication

class ThemeManager:
    def __init__(self, app: QApplication):
        self.app = app
        self.dark_mode = False
        self.load_theme()

    def load_theme(self):
        theme_file = "assets/styles/spotify.qss" if self.dark_mode else "assets/styles/spotify_light.qss"
        file = QFile(theme_file)
        if file.exists():
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            stylesheet = stream.readAll()
            self.app.setStyleSheet(stylesheet)
            file.close()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.load_theme()
