import lyricsgenius

from spotify_client import SpotifyClient
from auth_token import AuthToken

class LyricsFinder:

    def __init__(self):
        a = AuthToken()
        self.lyrics_token = a.get_lyrics_genius_token()
        self.lyrics_genius = lyricsgenius.Genius(self.lyrics_token)
        self.spotify_client = SpotifyClient()

    def get_playlist_name(self, playlist_dict, playlist_index):
        return list(playlist_dict.keys())[playlist_index]

    def get_artist(self, playlist_dict, playlist_name, artist_index):
        return list((playlist_dict[playlist_name][artist_index]).keys())[0]

    def get_song(self, playlist_dict, playlist_name, artist_index, artist):
        return playlist_dict[playlist_name][artist_index][artist]

    def get_lyrics(self, artist, song_title):
        return self.lyrics_genius.search_song(song_title, artist)

    def extract_all_lyrics(self, playlist_dict, playlist_name):
        lyrics = []
        index = 0
        playlist = playlist_dict[playlist_name]
        while index < len(playlist):
            artist = self.get_artist(playlist_dict, playlist_name, index)
            song = self.get_song(playlist_dict, playlist_name, index, artist)
            lyric = self.get_lyrics(artist, song)
            lyrics.append(lyric.lyrics)
            index += 1
        return lyrics

if __name__ == '__main__':
    client = SpotifyClient()
    playlists = client.get_playlist_collection()
    playlist_dict = client.get_playlist_dict(playlists)
    l = LyricsFinder()
    lyrics = l.extract_all_lyrics(playlist_dict, 'passing through')
    print(lyrics)
