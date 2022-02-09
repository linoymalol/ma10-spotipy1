class Album:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.songs = []

    def __repr__(self):
        return f'id: {self.id} name: {self.name} songs: {self.songs}'

    def add_song(self, song):
        self.songs.append(song)