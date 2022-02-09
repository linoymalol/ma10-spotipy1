from load_file.file_reader import read_files
from load_file.file_parser import albums_parser, songs_parser, artists_parser

class Main:
    list = read_files("C:\songs")
    print(songs_parser(list))
    print(albums_parser(list))
    print(artists_parser(list))