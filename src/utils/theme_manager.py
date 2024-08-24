from PyQt5.QtCore import QFile, QTextStream

class ThemeManager:
    def __init__(self, app):
        self.app = app
        self.is_dark_mode = False # Dark mode isn't that good yet! 
        self.load_theme()

    def load_theme(self):
        theme_file = "assets/styles/spotify.qss" if self.is_dark_mode else "assets/styles/spotify_light.qss"
        file = QFile(theme_file)
        if file.exists():
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            stylesheet = stream.readAll()
            self.app.setStyleSheet(stylesheet)
            file.close()

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.load_theme()
