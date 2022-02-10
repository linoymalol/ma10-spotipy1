from load_file.file_reader import read_files
from load_file.load_to_the_relevant_object import albums_load, songs_load, artists_load
from user.user import User
from user.free_user import Free_user
from user.premium_user import Premium_user
from search.search import get_all_albums, get_all_artists, get_songs_of_album, get_albums_names_of_artist, get_top_10
import const
class Main:

    user1 = Free_user("325", "linoy")
    user1.create_playlist("love", ", 03DcpryHcONqKi2uKXK5Ow, 086myS9r57YsLbJpU0TgK9")
    user1.create_playlist("love", "086myS9r57YsLbJpU0TgK9")
    user1.create_playlist("shower", ", 03DcpryHcONqKi2uKXK5Ow, 086myS9r57YsLbJpU0TgK9")
    print(user1)