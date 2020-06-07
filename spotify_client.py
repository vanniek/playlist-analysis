import json

import requests

from auth_token import AuthToken

class SpotifyClient:

    def __init__(self):
        self.auth_token = AuthToken()
        self.access_token = self.auth_token.get_access_token()

    def get_user_playlist_collection(self):
        url = "https://api.spotify.com/v1/me/playlists"
        request = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            }
        )

        return json.loads(json.dumps(request.json()))

    def get_playlist(self, playlist_id):
        url = "https://api.spotify.com/v1/playlists/{}".format(playlist_id)
        request = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            }
        )

        return json.loads(json.dumps(request.json()))

    def get_track(self, track_id):
        url = "https://api.spotify.com/v1/tracks/{}".format(track_id)
        request = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        return json.loads(json.dumps(request.json()))

if __name__ == '__main__':
    p = SpotifyClient()
    response = p.get_user_playlist_collection()
    songs = p.get_playlist("3sPFyyILp6d1Zc6SwCq9qH")
    song = p.get_track("1w3QqUDJ4X339XBGjEJqdX")
    print(response)
    # print(response.json())

