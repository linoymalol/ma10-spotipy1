from load_file.file_reader import read_files
from load_file.load_to_the_relevant_object import albums_load, songs_load, artists_load
from user.user import User
from search.search import get_all_albums, get_all_artists, get_songs_of_album, get_albums_names_of_artist, get_top_10

class Main:
   # print(get_all_artists())
    user1 = User("325", "linoy")
    user1.create_playlist("love", "123, 345")
    user1.create_playlist("love", "123, 345")

    print(user1)