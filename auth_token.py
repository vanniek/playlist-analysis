import json
import requests
from secrets import client_secret, client_id, lyrics_genius_token

class AuthToken:

    def __init__(self):
        self.client_secret = client_secret
        self.client_id = client_id
        self.lyrics_genius_token = lyrics_genius_token

    def post_auth_token(self):
        grant_type = 'client_credentials'
        url = "https://accounts.spotify.com/api/token"
        return requests.post(
            url,
            data={
                'grant_type': grant_type
            },
            auth=(client_id, client_secret)
        )

    def get_access_token(self):
        response = self.post_auth_token()
        resp = json.loads(json.dumps(response.json()))
        return resp['access_token']

    def get_lyrics_genius_token(self):
        return lyrics_genius_token

if __name__ == '__main__':
    p = AuthToken()
    auth_token = p.get_access_token()
    print(auth_token)
