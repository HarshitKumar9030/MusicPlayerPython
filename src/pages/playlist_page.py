from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel, QInputDialog, QListWidgetItem, QFileDialog

from src.utils.database_handler import DatabaseHandler

class PlaylistPage(QWidget):
    def __init__(self, parent=None, player_logic=None):
        super().__init__(parent)
        self.db = DatabaseHandler('database/music_player.db')
        self.player_logic = player_logic
        self.current_playlist = None

        layout = QVBoxLayout()

        self.playlist_title = QLabel("Your Playlists")
        layout.addWidget(self.playlist_title)

        self.refresh_playlists_button = QPushButton("Refresh Playlists")
        self.refresh_playlists_button.clicked.connect(self.load_playlists)
        layout.addWidget(self.refresh_playlists_button)

        self.playlist_list = QListWidget()
        self.playlist_list.itemClicked.connect(self.load_playlist)
        layout.addWidget(self.playlist_list)

        self.song_list = QListWidget()
        self.song_list.itemClicked.connect(self.play_song)
        layout.addWidget(QLabel("Songs in Playlist"))
        layout.addWidget(self.song_list)

        self.refresh_songs_button = QPushButton("Refresh Songs")
        self.refresh_songs_button.clicked.connect(lambda: self.load_playlist(self.playlist_list.currentItem()))
        layout.addWidget(self.refresh_songs_button)

        self.add_playlist_button = QPushButton("Add New Playlist")
        self.add_playlist_button.clicked.connect(self.add_new_playlist)
        layout.addWidget(self.add_playlist_button)

        self.add_song_to_playlist_button = QPushButton("Add Song to Playlist")
        self.add_song_to_playlist_button.clicked.connect(self.add_song_to_playlist)
        layout.addWidget(self.add_song_to_playlist_button)

        self.setLayout(layout)
        self.load_playlists()

    def load_playlists(self):
        self.playlist_list.clear()
        playlists = self.db.get_playlists()
        for playlist in playlists:
            item = QListWidgetItem(playlist['name'])
            item.setData(1, playlist['id'])
            self.playlist_list.addItem(item)

    def load_playlist(self, item):
        if item is None:
            return
        playlist_id = item.data(1)
        self.current_playlist = playlist_id
        self.song_list.clear()
        songs = self.db.get_songs_by_playlist(playlist_id)
        self.player_logic.current_playlist = [song['file_path'] for song in songs]
        for song in songs:
            song_item = QListWidgetItem(f"{song['title']} - {song['artist']}")
            song_item.setData(1, song['file_path'])  # Store the file path for playback
            self.song_list.addItem(song_item)

    def add_new_playlist(self):
        playlist_name, ok = QInputDialog.getText(self, "New Playlist", "Enter playlist name:")
        if ok and playlist_name:
            self.db.create_playlist(playlist_name)
            self.load_playlists()

    def add_song_to_playlist(self):
        if self.current_playlist is None:
            return

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Song", "", "Audio Files (*.mp3 *.wav)")
        if not file_path:
            return

        song_title, ok_title = QInputDialog.getText(self, "Song Title", "Enter song title:")
        if not ok_title or not song_title:
            return

        song_artist, ok_artist = QInputDialog.getText(self, "Song Artist", "Enter song artist:")
        if not ok_artist or not song_artist:
            song_artist = "Unknown Artist"

        self.db.add_song_to_playlist(self.current_playlist, song_title, song_artist, file_path)
        self.load_playlist(self.playlist_list.currentItem())

    def play_song(self, item):
        if item is None:
            return
        file_path = item.data(1)
        self.player_logic.play_music(file_path)
