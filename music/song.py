class Song:
    def __init__(self, id, name, popularity):
        self.id = id
        self.name = name
        self.popularity = popularity

    def __repr__(self):
        return f' name: {self.name} popularity: {self.popularity}'
