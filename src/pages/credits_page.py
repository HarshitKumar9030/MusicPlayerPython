from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class CreditsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Credits"))
        self.layout.addWidget(QLabel("App created by: Your Name"))
        self.layout.addWidget(QLabel("Inspired by Spotify UI"))
        self.layout.addWidget(QLabel("Icons from: Icon Provider"))
        self.layout.addWidget(QLabel("Libraries used: PyQt5, pygame, SQLite"))

        self.setLayout(self.layout)
