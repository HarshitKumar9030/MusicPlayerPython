from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer
from src.utils.database_handler import DatabaseHandler

class PlayerLogic:
    def __init__(self):
        self.db = DatabaseHandler('database/music_player.db')
        self.media_player = QMediaPlayer()
        self.current_playlist = []
        self.current_index = 0
        self.is_looping = False
        self.is_shuffling = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    def add_song(self, parent):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(parent, "Select Song", "", "Audio Files (*.mp3 *.wav)")

        if file_path:
            song_title, ok_title = QInputDialog.getText(parent, "Song Title", "Enter the song title:")
            if not ok_title:
                return

            song_artist, ok_artist = QInputDialog.getText(parent, "Song Artist", "Enter the song artist:")
            if not ok_artist:
                song_artist = "Unknown Artist"

            self.db.add_song_to_playlist(None, song_title, song_artist, file_path)
            print(f"Song added: {song_title} by {song_artist}")

    def load_songs(self):
        return self.db.get_songs()

    def get_playlists(self):
        return self.db.get_playlists()

    def load_songs_by_playlist(self, playlist_id):
        return self.db.get_songs_by_playlist(playlist_id)

    def play_music(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        content = QMediaContent(url)
        self.media_player.setMedia(content)
        self.media_player.play()
        self.timer.start(1000) 

    def pause_music(self):
        self.media_player.pause()
        self.timer.stop()

    def stop_music(self):
        self.media_player.stop()
        self.timer.stop()

    def update_progress(self):
        pass

    def play_next(self):
        if self.is_shuffling:
            self.current_index = random.randint(0, len(self.current_playlist) - 1)
        else:
            self.current_index = (self.current_index + 1) % len(self.current_playlist)

        if self.is_looping:
            self.play_music(self.current_playlist[self.current_index])
        else:
            self.play_music(self.current_playlist[self.current_index])

    def play_previous(self):
        self.current_index = (self.current_index - 1) % len(self.current_playlist)
        self.play_music(self.current_playlist[self.current_index])

    def enable_loop(self):
        self.is_looping = True

    def disable_loop(self):
        self.is_looping = False

    def enable_shuffle(self):
        self.is_shuffling = True

    def disable_shuffle(self):
        self.is_shuffling = False
