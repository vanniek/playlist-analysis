import lyricsgenius
import re

import nltk

from spotify_client import SpotifyClient
from auth_token import AuthToken

REPLACE_NO_SPACE = re.compile("[.;&:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

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
            if lyric == None:
                cleaned_lyrics = self.clean_lyrics("")
            else:
                cleaned_lyrics = self.clean_lyrics(lyric.lyrics)
            lyrics += cleaned_lyrics
            index += 1
        return lyrics

    def extract_complete_lyrics(self, playlist_dict):
        lyrics = []
        index = 0
        i = 0
        for playlist_name in playlist_dict.keys():
            if i == 8:
                break
            else:
                playlist = playlist_dict[playlist_name]
                while index < len(playlist):
                    artist = self.get_artist(playlist_dict, playlist_name, index)
                    song = self.get_song(playlist_dict, playlist_name, index, artist)
                    lyric = self.get_lyrics(artist, song)
                    if lyric == None:
                        cleaned_lyrics = self.clean_lyrics("")
                    else:
                        cleaned_lyrics = self.clean_lyrics(lyric.lyrics)
                    lyrics += cleaned_lyrics
                    index += 1
                    i += 1
        return lyrics

    def clean_lyrics(self, lyrics):
        lyrics = [REPLACE_NO_SPACE.sub("", line.lower()) for line in lyrics]
        lyrics = [REPLACE_WITH_SPACE.sub(" ", line) for line in lyrics]
        l = ""
        for ly in lyrics:
            l += ly

        cleaned_lyrics = l.replace("verse 1", "")
        cleaned_lyrics = cleaned_lyrics.replace("chorus", "")
        cleaned_lyrics = cleaned_lyrics.replace("intro", "")
        cleaned_lyrics = cleaned_lyrics.replace("verse 2", "")
        cleaned_lyrics = cleaned_lyrics.replace("outro", "")

        return cleaned_lyrics.split()


if __name__ == '__main__':
    client = SpotifyClient()
    playlists = client.get_playlist_collection()
    playlist_dict = client.get_playlist_dict(playlists)
    l = LyricsFinder()
    lyrics = l.extract_all_lyrics(playlist_dict, 'passing through')
    print(lyrics)
