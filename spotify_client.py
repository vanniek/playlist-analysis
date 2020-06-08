from spotify_service import SpotifyService

class SpotifyClient:

    def __init__(self):
        self.service = SpotifyService()

    def get_playlist_collection(self):
        playlist_collection = {}
        spotify_song_payload = self.service.get_user_playlist_collection()
        playlist_items = spotify_song_payload['items']
        for playlist in playlist_items:
            playlist_collection[playlist['id']] = playlist['name']

        return playlist_collection

    def get_playlist_dict(self, playlist_collection):
        playlist_dict = {}
        for playlist_id in playlist_collection:
            tracks = self.service.get_playlist(playlist_id)['tracks']
            songs_list = tracks['items']
            track_ids = []
            i = 0
            while i < len(songs_list):
                song_dict = {}
                artist = songs_list[i]['track']['artists'][0]['name']
                track_name = songs_list[i]['track']['name']
                song_dict[artist] = track_name
                track_ids.append(song_dict)
                i += 1
            playlist_dict[playlist_collection[playlist_id]] = track_ids

        return playlist_dict

if __name__ == '__main__':
    client = SpotifyClient()
    playlists = client.get_playlist_collection()
    playlist_dict = client.get_playlist_dict(playlists)
    print(playlist_dict)
