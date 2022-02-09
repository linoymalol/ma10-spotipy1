class Artist:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.albums = []

    def __repr__(self):
        return f'id: {self.id} name: {self.name} albums: {self.albums}'

    def add_album(self, album):
        self.albums.append(album)