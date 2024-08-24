from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap
from PyQt5.QtCore import Qt

class CreditsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        font_id = QFontDatabase.addApplicationFont("assets/fonts/Montserrat-VariableFont_wght.ttf")
        if font_id == -1:
            print("Error: Font could not be loaded. Using default font.")
            font_family = "Arial" 
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0] 

        self.default_font = QFont(font_family, 16)
        self.layout = QVBoxLayout()

        title_label = QLabel("Credits")
        title_label.setFont(QFont(font_family, 28, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #1DB954; padding: 20px;")

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #1DB954; margin: 15px 0;")

        dev_info_layout = QHBoxLayout()
        dev_icon = QLabel()
        dev_icon.setPixmap(QPixmap("assets/icons/author.svg").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        dev_icon.setAlignment(Qt.AlignCenter)
        
        developer_label = QLabel("App created by: Harshit")
        developer_label.setFont(QFont(font_family, 20, QFont.Bold))
        developer_label.setAlignment(Qt.AlignLeft)
        developer_label.setStyleSheet("color: #FFFFFF; margin-left: 10px;")

        dev_info_layout.addWidget(dev_icon)
        dev_info_layout.addWidget(developer_label)
        dev_info_layout.addStretch()

        links_layout = QVBoxLayout()

        website_label = QLabel('<a href="https://leoncyriac.me">Website: leoncyriac.me</a>')
        website_label.setFont(QFont(font_family, 16))
        website_label.setAlignment(Qt.AlignCenter)
        website_label.setStyleSheet("color: #1DB954;")
        website_label.setOpenExternalLinks(True)

        x_label = QLabel('<a href="https://twitter.com/OhHarshit">X (Twitter): @OhHarshit</a>')
        x_label.setFont(QFont(font_family, 16))
        x_label.setAlignment(Qt.AlignCenter)
        x_label.setStyleSheet("color: #1DB954;")
        x_label.setOpenExternalLinks(True)

        insta_label = QLabel('<a href="https://instagram.com/_harshit.xd">Instagram: @_harshit.xd</a>')
        insta_label.setFont(QFont(font_family, 16))
        insta_label.setAlignment(Qt.AlignCenter)
        insta_label.setStyleSheet("color: #1DB954;")
        insta_label.setOpenExternalLinks(True)

        links_layout.addWidget(website_label)
        links_layout.addWidget(x_label)
        links_layout.addWidget(insta_label)
        links_layout.addStretch()



        
        libraries_label = QLabel("Libraries used: PyQt5, pygame, SQLite")
        libraries_label.setFont(QFont(font_family, 14))
        libraries_label.setAlignment(Qt.AlignCenter)
        libraries_label.setStyleSheet("color: #B3B3B3; margin-top: 10px;")

        self.layout.addWidget(title_label)
        self.layout.addWidget(separator)
        self.layout.addLayout(dev_info_layout)
        self.layout.addLayout(links_layout)
        self.layout.addWidget(libraries_label)
        self.layout.addStretch()

        self.setLayout(self.layout)
