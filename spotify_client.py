import requests
from secrets import api_token

class SpotifyClient:

    def __init__(self):
        self.api_token = api_token

    def get_user_playlist_collection(self):
        url = "https://api.spotify.com/v1/me/playlists"
        return requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

    def get_playlist(self, playlist_id):
        url = "https://api.spotify.com/v1/playlists/{}".format(playlist_id)
        return requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

    def get_track(self, track_id):
        url = "https://api.spotify.com/v1/tracks/{}".format(track_id)
        return requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

if __name__ == '__main__':
    p = SpotifyClient()
    response = p.get_user_playlist_collection()
    songs = p.get_playlist("3sPFyyILp6d1Zc6SwCq9qH")
    song = p.get_track("1w3QqUDJ4X339XBGjEJqdX")
    print(song.json())
    # print(response.json())

