from music.album import Album
from music.artist import Artist
from music.song import Song
from logs.logging import info_log, debug_log, warning_log, error_log

def albums_load(data_files):
    info_log(__name__, albums_load.__name__, "Entered into the function")
    all_albums = {}
    for data_file in data_files:
        songs = data_file.get('track')
        albums = songs.get('album')
        for album in albums:
            if album not in all_albums.keys():
                new_album = Album(songs.get('album').get('id'), songs.get('album').get('name'))
                Album.add_song(new_album, songs.get('id'))
                all_albums[new_album.id] = (new_album)
            else:
                Album.add_song(songs.get('album'), songs.get('id'))
    info_log(__name__, albums_load.__name__, "The function ended successfully")
    return all_albums


def artists_load(data_files):
    info_log(__name__, artists_load.__name__, "Entered into the function")
    all_artists = {}
    for data_file in data_files:
        songs = data_file.get('track')
        artists = songs.get('artists')
        for artist in artists:
            if artist.get('id') not in all_artists.keys():
                new_artist = Artist(artist.get('id'), artist.get('name'))
                Artist.add_album(new_artist, songs.get('album'))
                all_artists[artist.get('id')] = new_artist
            else:
                Artist.add_album(all_artists.get(artist.get('id')), songs.get('album'))
    info_log(__name__, artists_load.__name__, "The function ended successfully")
    return all_artists


def songs_load(data_files):
    info_log(__name__, songs_load.__name__, "Entered into the function")
    all_songs = {}
    for data_file in data_files:
        songs = data_file.get('track')
        all_songs[songs.get('id')] = Song(songs.get('id'), songs.get('name'),songs.get('popularity'))
    info_log(__name__, songs_load.__name__, "The function ended successfully")
    return all_songs
