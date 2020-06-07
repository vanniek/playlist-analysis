import json
import lyricsgenius

from spotify_client import SpotifyClient
from auth_token import AuthToken

class LyricsFinder:

    def __init__(self):
        a = AuthToken()
        self.lyrics_token = a.get_lyrics_genius_token()
        self.lyrics_genius = lyricsgenius.Genius(self.lyrics_token)

    def get_song(self, spotify_song_payload):
        return spotify_song_payload['name']

    def get_artist(self, spotify_song_payload):
        return spotify_song_payload['artists'][0]['name']

    def get_lyrics(self, artist, song_title):
        return self.lyrics_genius.search_song(song_title, artist)

if __name__ == '__main__':
    p = SpotifyClient()
    response = p.get_user_playlist_collection()
    songs = p.get_playlist("3sPFyyILp6d1Zc6SwCq9qH")
    song = p.get_track("1w3QqUDJ4X339XBGjEJqdX")
    l = LyricsFinder()
    artist = l.get_artist(song)
    track = l.get_song(song)
    lyrics = l.get_lyrics(artist, track)
    print(lyrics)
