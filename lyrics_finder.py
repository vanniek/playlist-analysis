import lyricsgenius
import re
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
            cleaned_lyrics = self.clean_lyrics(lyric.lyrics)
            lyrics.append(cleaned_lyrics)
            index += 1
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
    # lyrics = "[Verse 1]\nIn another time, in another place\nYou would be mine\nOn a brighter day, under a different\u2005sky\nMaybe\u2005we'd fly\n\n[Chorus]\nGood girl,\u2005I knew you were a good\u2005girl\nThat's all I ever fall for, the kind I lose it all for\nYes, I was in the wrong place at the wrong time with the right one\nNow you think you're tryna help, oh\nBut you can't save me from myself, ooh\nNo, you can't save me from myself, ooh, ooh\n\n[Verse 2]\nI keep reminding myself\nI wasn't here for the view\nJust 'cause we seem like we care\nDidn't really mean that we care\nI didn't run from the truth\nI was just keepin' it real\nAnd our conversation was good, ooh\n\n[Chorus]\n'Cause you're a good girl, I knew you were a good girl\nThat's all I ever fall for, the kind I lose it all for\nYes, I was in the wrong place at the wrong time with the right one\nNow you think you're tryna help\nBut you can't save me from myself, ooh\nNo, you can't save me from myself, ooh, ooh\n[Outro]\nThat was reasonable"
    # ly = l.clean_lyrics(lyrics)
    lyrics = l.extract_all_lyrics(playlist_dict, 'passing through')
    print(lyrics)
