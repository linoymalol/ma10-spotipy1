from logs.logging import info_log, debug_log, warning_log, error_log
class Artist:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.albums = {}

    def __repr__(self):
        return f'name: {self.name} albums: {self.albums} '

    #logs here?
    def add_album(self, album):
        #info_log(__name__, self.add_album.__name__, "Entered into the function")
        self.albums[album.get('id')] = album.get('name')
        #info_log(__name__, self.add_album.__name__, "The function ended successfully")