import sqlite3

class DatabaseHandler:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.setup_tables()

    def setup_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS playlists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                artist TEXT,
                file_path TEXT,
                playlist_id INTEGER
            )
        ''')
        self.connection.commit()

    def get_playlists(self):
        self.cursor.execute('SELECT * FROM playlists')
        return [{'id': row[0], 'name': row[1]} for row in self.cursor.fetchall()]

    def get_songs_by_playlist(self, playlist_id):
        self.cursor.execute('SELECT * FROM songs WHERE playlist_id = ?', (playlist_id,))
        return [{'title': row[1], 'artist': row[2], 'file_path': row[3]} for row in self.cursor.fetchall()]

    def add_song_to_playlist(self, playlist_id, title, artist, file_path):
        self.cursor.execute('INSERT INTO songs (title, artist, file_path, playlist_id) VALUES (?, ?, ?, ?)',
                            (title, artist, file_path, playlist_id))
        self.connection.commit()

        
    def get_songs(self):
        self.cursor.execute('SELECT * FROM songs')
        return [{'title': row[1], 'artist': row[2], 'file_path': row[3]} for row in self.cursor.fetchall()]


    def create_playlist(self, name):
        self.cursor.execute('INSERT INTO playlists (name) VALUES (?)', (name,))
        self.connection.commit()

    def close(self):
        self.connection.close()
