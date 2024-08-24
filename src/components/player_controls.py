from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QSlider
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class PlayerControls(QWidget):
    def __init__(self, parent=None, player_logic=None):
        super().__init__(parent)
        self.player_logic = player_logic
        self.is_playing = False
        self.is_looping = False
        self.is_shuffling = False

        layout = QHBoxLayout()

        prev_btn = QPushButton()
        prev_btn.setIcon(QIcon("assets/icons/previous.svg"))
        prev_btn.setToolTip("Previous")
        prev_btn.clicked.connect(self.player_logic.play_previous)
        layout.addWidget(prev_btn)

        self.play_pause_btn = QPushButton()
        self.play_pause_btn.setIcon(QIcon("assets/icons/play.svg"))
        self.play_pause_btn.setToolTip("Play")
        self.play_pause_btn.clicked.connect(self.toggle_play_pause)
        layout.addWidget(self.play_pause_btn)

        next_btn = QPushButton()
        next_btn.setIcon(QIcon("assets/icons/next.svg"))
        next_btn.setToolTip("Next")
        next_btn.clicked.connect(self.player_logic.play_next)
        layout.addWidget(next_btn)

        self.loop_btn = QPushButton()
        self.loop_btn.setIcon(QIcon("assets/icons/loop.svg"))
        self.loop_btn.setToolTip("Loop")
        self.loop_btn.clicked.connect(self.toggle_loop)
        layout.addWidget(self.loop_btn)

        self.shuffle_btn = QPushButton()
        self.shuffle_btn.setIcon(QIcon("assets/icons/shuffle.svg"))
        self.shuffle_btn.setToolTip("Shuffle")
        self.shuffle_btn.clicked.connect(self.toggle_shuffle)
        layout.addWidget(self.shuffle_btn)

        self.song_progress = QSlider(Qt.Horizontal)
        self.song_progress.setToolTip("Seek")
        layout.addWidget(self.song_progress)

        self.timestamp_label = QLabel("0:00 / 0:00")
        layout.addWidget(self.timestamp_label)

        self.setLayout(layout)

        self.player_logic.set_progress_elements(self.song_progress, self.timestamp_label)

    def toggle_play_pause(self):
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.play_pause_btn.setIcon(QIcon("assets/icons/pause.svg"))
            self.play_pause_btn.setToolTip("Pause")
            self.player_logic.play_music(self.player_logic.current_playlist[self.player_logic.current_index])
        else:
            self.play_pause_btn.setIcon(QIcon("assets/icons/play.svg"))
            self.play_pause_btn.setToolTip("Play")
            self.player_logic.pause_music()

    def toggle_loop(self):
        self.is_looping = not self.is_looping
        if self.is_looping:
            self.loop_btn.setStyleSheet("background-color: #1DB954;")
            self.loop_btn.setToolTip("Looping Enabled")
            self.player_logic.enable_loop()
        else:
            self.loop_btn.setStyleSheet("")
            self.loop_btn.setToolTip("Loop")
            self.player_logic.disable_loop()

    def toggle_shuffle(self):
        self.is_shuffling = not self.is_shuffling
        if self.is_shuffling:
            self.shuffle_btn.setStyleSheet("background-color: #1DB954;")
            self.shuffle_btn.setToolTip("Shuffling Enabled")
            self.player_logic.enable_shuffle()
        else:
            self.shuffle_btn.setStyleSheet("")
            self.shuffle_btn.setToolTip("Shuffle")
            self.player_logic.disable_shuffle()
