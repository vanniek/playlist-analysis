import nltk

from lyrics_finder import LyricsFinder
from spotify_client import SpotifyClient


class LyricsAnalysis:

    def __init__(self):
        pass

    def tokenize(self, cleaned_lyrics):
        token = []
        for word in cleaned_lyrics:
            token.append(word)
        return token

    def analyse(self, tokens):
        from nltk.corpus import stopwords
        additional_words = ['another', 'huh', 'yeah', 'know', 'like', 'oh', 'dont', 'im', 'youre', 'two', 'ooh', 'cant',
                            'cause', 'something', 'way', 'would', 'hmm', 'make', 'aint', 'daniel', 'wanna', 'wasnt',
                            'mm', 'one', 'daley', 'thats', 'tryna', 'pre', 'gotta', 'kiana', 'feat', 'gon', 'ima',
                            'could', 'get', 'i`m', 'lets', 'ah', 'nah']
        all_stopwords = stopwords.words('english')
        all_stopwords.extend(additional_words)
        all_stopwords.extend(stopwords.words('french'))
        sr = stopwords.words('english')
        clean_tokens = tokens[:]
        for token in tokens:
            if token in all_stopwords:
                clean_tokens.remove(token)
        freq = nltk.FreqDist(clean_tokens)
        for key, val in freq.items():
            print(str(key) + ':' + str(val))
        freq.plot(50, cumulative=False)

if __name__ == '__main__':
    a = LyricsAnalysis()
    client = SpotifyClient()
    playlists = client.get_playlist_collection()
    playlist_dict = client.get_playlist_dict(playlists)
    l = LyricsFinder()
    lyrics = l.extract_all_lyrics(playlist_dict, 'rainy nights in toronto ☔️')
    print(lyrics)
    token = a.tokenize(lyrics)
    a.analyse(token)

