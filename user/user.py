from load_file.load_to_the_relevant_object import songs_load
from load_file.file_reader import read_files
from logs.logging import info_log, debug_log, warning_log, error_log
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.playlists = {}

    def __repr__(self):
        return f'id: {self.id} name: {self.name} playlist: {self.playlists}'
    def create_playlist(self, name, songs):
        info_log(__name__, self.create_playlist.__name__, "Entered into the function")
        if name not in self.playlists.keys():
            self.playlists[name] = songs
            info_log(__name__, self.create_playlist.__name__, "The function ended successfully")
        else:
            error_log(__name__, self.create_playlist.__name__, "the playlist name already exist")