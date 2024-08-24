from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel

class PlaylistView(QWidget):
    def __init__(self, playlist_name, songs, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        # Playlist Title
        self.layout.addWidget(QLabel(playlist_name))

        # Song List
        self.song_list = QListWidget()
        for song in songs:
            self.song_list.addItem(f"{song['title']} - {song['artist']}")

        self.layout.addWidget(self.song_list)
        self.setLayout(self.layout)
