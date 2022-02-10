from logs.logging import info_log, debug_log, warning_log, error_log
class Album:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.songs = []

    def __repr__(self):
        return f'name: {self.name} songs: {self.songs}'

    # logs here?
    def add_song(self, song):
        #info_log(__name__, self.add_song.__name__, "Entered into the function")
        self.songs.append(song)
        #info_log(__name__, self.add_song.__name__, "The function ended successfully")