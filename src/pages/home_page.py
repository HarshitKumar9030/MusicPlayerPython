from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel

class HomePage(QWidget):
    def __init__(self, parent=None, player_logic=None):
        super().__init__(parent)
        self.player_logic = player_logic
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Your Library"))

        self.song_list = QListWidget()
        self.song_list.itemClicked.connect(self.play_song)
        self.layout.addWidget(self.song_list)

        self.add_song_btn = QPushButton("Add Song")
        self.add_song_btn.clicked.connect(parent.add_song)
        self.layout.addWidget(self.add_song_btn)

        self.refresh_btn = QPushButton("Refresh Library")
        self.refresh_btn.clicked.connect(self.load_songs)
        self.layout.addWidget(self.refresh_btn)

        self.load_songs()
        self.setLayout(self.layout)

    def load_songs(self):
        self.song_list.clear()
        songs = self.player_logic.load_songs()
        self.player_logic.current_playlist = [song['file_path'] for song in songs]
        for song in songs:
            song_item = QListWidgetItem(f"{song['title']} - {song['artist']}")
            song_item.setData(1, song['file_path'])
            self.song_list.addItem(song_item)

    def play_song(self, item):
        if item is None:
            return
        file_path = item.data(1)
        self.player_logic.play_music(file_path)
