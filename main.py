import sys
import os
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        pygame.mixer.init()

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()

        self.playlist = QListWidget()
        layout.addWidget(self.playlist)

        controls_layout = QHBoxLayout()

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_music)
        controls_layout.addWidget(self.play_button)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_music)
        controls_layout.addWidget(self.pause_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_music)
        controls_layout.addWidget(self.stop_button)

        layout.addLayout(controls_layout)

        # Add song button
        self.add_song_button = QPushButton("Add Song")
        self.add_song_button.clicked.connect(self.add_song)
        layout.addWidget(self.add_song_button)

        self.setLayout(layout)

        self.current_song = None

    def add_song(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Song", "", "Audio Files (*.mp3 *.wav)")
        if file_path:
            self.playlist.addItem(file_path)

    def play_music(self):
        if self.playlist.count() > 0:
            selected_song = self.playlist.currentItem()
            if selected_song:
                song_path = selected_song.text()
                if self.current_song != song_path:
                    pygame.mixer.music.load(song_path)
                    pygame.mixer.music.play()
                    self.current_song = song_path
                else:
                    pygame.mixer.music.unpause()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
