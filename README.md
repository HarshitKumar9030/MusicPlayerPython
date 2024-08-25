# Spotify-Inspired Music Player

![player](https://github.com/user-attachments/assets/08f7346e-8c2d-44c3-b1e8-0780201cf4c5)

A sleek, modern music player inspired by Spotify’s UI, built using Python and PyQt5. The app features playlist management, song playback controls (play, pause, shuffle, loop), a dynamic UI with theme switching, and more.

## Features

- 🎵 **Play/Pause/Skip**: Control your music playback with intuitive buttons.
- 🎚️ **Seek and Progress Bar**: Easily navigate through songs with a responsive seek bar.
- 🔄 **Loop and Shuffle**: Repeat songs or shuffle through your playlists.
- 📃 **Playlist Management**: Create, manage, and edit playlists with ease.
- 🌗 **Theme Switching**: Switch between light and dark modes with smooth transitions.
- 📜 **Credits Page**: A stylized credits page showcasing the developer and resources used.

## Getting Started

### Prerequisites

- Python 3.x
- PyQt5

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HarshitKumar9030/MusicPlayerPython.git
   cd MusicPlayerPython
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## Folder Structure

```
MusicPlayerPython/
│
├── assets/
│   ├── fonts/           # Contains Montserrat font files
│   ├── icons/           # Contains SVG icons used in the UI
│   └── styles/          # QSS stylesheets for light and dark themes
│
├── database/
│   └── music_player.db  # SQLite database for storing playlists and songs
│
├── src/
│   ├── components/      # Sidebar, player controls, theme switcher, etc.
│   ├── pages/           # Home, playlist, credits, and settings pages
│   ├── utils/           # Helper functions and logic handlers
│   └── main.py          # Main entry point for the application
│
└── README.md            # Project documentation
```

## Contributions

We welcome contributions from the community! Here’s how you can get involved:

1. **Fork the repository** and clone it locally.
2. Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b feature/my-new-feature
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add my new feature"
   ```

4. Push your branch to your fork:

   ```bash
   git push origin feature/my-new-feature
   ```

5. Open a pull request and describe your changes.

## Issues and Bug Reports

If you encounter any issues, please [open an issue](https://github.com/HarshitKumar9030/MusicPlayerPython/issues) on GitHub. Provide detailed steps to reproduce the problem, along with screenshots or error messages if applicable.

## Credits

- **Developer**: Harshit (leoncyriac.me)
- **Socials**: [X (Twitter): @OhHarshit](https://twitter.com/OhHarshit) | [Instagram: @\_harshit.xd](https://instagram.com/_harshit.xd)
- **Icons**: Icons are sourced from svgrepo.
- **Libraries Used**: PyQt5, pygame, SQLite

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
