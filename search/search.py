from load_file.load_to_the_relevant_object import artists_load, albums_load
from load_file.file_reader import read_files
import const
from logs.logging import info_log, debug_log, warning_log, error_log


def get_all_artists():
    info_log(__name__, get_all_artists.__name__, "Entered into the function")
    data_files = read_files(const.PATH)
    artists = artists_load(data_files)
    info_log(__name__, get_all_artists.__name__, "The function ended successfully")
    return artists


def get_all_albums():
    info_log(__name__, get_all_albums.__name__, "Entered into the function")
    data_files = read_files(const.PATH)
    albums = albums_load(data_files)
    info_log(__name__, get_all_albums.__name__, "The function ended successfully")
    return albums


def get_albums_of_artist(artist_id):
    info_log(__name__, get_albums_of_artist.__name__, "Entered into the function")
    all_artists = get_all_artists()
    artist = all_artists.get(artist_id)
    artist_albums = artist.albums
    info_log(__name__, get_albums_of_artist.__name__, "The function ended successfully")
    return artist_albums


def get_albums_names_of_artist(artist_id):
    info_log(__name__, get_albums_names_of_artist.__name__, "Entered into the function")
    albums_names = get_albums_of_artist(artist_id).values()
    info_log(__name__, get_albums_names_of_artist.__name__, "The function ended successfully")
    return albums_names


# TO DO: complete the function
def get_top_10(artist_id):
    info_log(__name__, get_top_10.__name__, "Entered into the function")
    albums_of_artist = get_albums_of_artist(artist_id)
    popular_songs = {}
    for album in albums_of_artist.items():
        for song in album:
            popular_songs[song.id] = song.popularity
    sorted_songs = sorted(popular_songs.items(), key=lambda x: x[1], reverse=True)
    return


def get_songs_of_album(album_id):
    info_log(__name__, get_songs_of_album.__name__, "Entered into the function")
    all_albums = get_all_albums()
    album = all_albums.get(album_id)
    album_songs = album.songs
    info_log(__name__, get_songs_of_album.__name__, "The function ended successfully")
    return album_songs
