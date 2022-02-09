from music.album import Album
from music.artist import Artist
from music.song import Song


def albums_parser(data_files):
    all_albums = []
    for data_file in data_files:
        songs = data_file.get('track')
        if songs.get('album') not in all_albums:
            new_album = Album(songs.get('album').get('id'), songs.get('album').get('name'))
            Album.add_song(new_album, songs.get('id'))
            all_albums.append(new_album)
        else:
            Album.add_song(songs.get('album'), songs.get('id'))
    return all_albums

def artists_parser(data_files):
    all_artists = []
    for data_file in data_files:
        songs = data_file.get('track')
        artists = songs.get('artists')
        for artist in artists:
            if artist not in all_artists:
                new_artist = Artist(artist.get('id'), artist.get('name'))
                Artist.add_album(new_artist, songs.get('id'))
                all_artists.append(new_artist)
            else:
                Artist.add_album(artist, songs.get('id'))

    return all_artists

def songs_parser(data_files):
    all_songs = []
    for data_file in data_files:
        songs = data_file.get('track')
        all_songs.append(Song(songs.get('id'), songs.get('name'),
                              songs.get('popularity')))
    return all_songs
