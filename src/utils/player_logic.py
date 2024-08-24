from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from src.utils.database_handler import DatabaseHandler
from src.utils.time_formatter import format_time
import random

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
        self.timer.start(1000)

        self.progress_bar = None
        self.timestamp_label = None
        self.is_seeking = False

        self.current_song = None

        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

    def set_progress_elements(self, progress_bar, timestamp_label):
        self.progress_bar = progress_bar
        self.timestamp_label = timestamp_label
        if self.progress_bar:
            self.progress_bar.sliderReleased.connect(self.seek_position)

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

    def play_music(self, file_path=None):
        if file_path is None:
            file_path = self.current_playlist[self.current_index]

        if self.current_song == file_path and self.media_player.state() == QMediaPlayer.PausedState:
            self.media_player.play()
        else:
            url = QUrl.fromLocalFile(file_path)
            content = QMediaContent(url)
            self.media_player.setMedia(content)
            self.media_player.play()

            if self.progress_bar:
                self.progress_bar.setValue(0)
                self.progress_bar.setMaximum(self.media_player.duration() // 1000)

            self.current_song = file_path
            self.current_index = self.current_playlist.index(file_path)

    def pause_music(self):
        self.media_player.pause()

    def stop_music(self):
        self.media_player.stop()

    def update_progress(self):
        if not self.is_seeking:
            if self.media_player.state() == QMediaPlayer.PlayingState:
                current_position = self.media_player.position() // 1000
                total_duration = self.media_player.duration() // 1000

                if self.progress_bar:
                    self.progress_bar.setValue(current_position)

                if self.timestamp_label:
                    self.timestamp_label.setText(f"{format_time(current_position)} / {format_time(total_duration)}")

    def play_next(self):
        if self.is_shuffling:
            self.current_index = random.randint(0, len(self.current_playlist) - 1)
        else:
            self.current_index = (self.current_index + 1) % len(self.current_playlist)

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

    def seek_position(self):
        if self.progress_bar:
            position = self.progress_bar.value()
            self.is_seeking = True
            self.media_player.setPosition(position * 1000)
            self.is_seeking = False

    def position_changed(self, position):
        if not self.is_seeking and self.progress_bar:
            self.progress_bar.setValue(position // 1000)

    def duration_changed(self, duration):
        if self.progress_bar:
            self.progress_bar.setMaximum(duration // 1000)
