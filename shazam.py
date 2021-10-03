import os

import requests


def rec_shazam(query) -> list:
    API_KEY = os.getenv("SHAZAM")
    url = "https://shazam.p.rapidapi.com/search"

    querystring = {"term": query, "locale": "en-US", "offset": "0", "limit": "5"}

    headers = {
        'x-rapidapi-host': "shazam.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return [f"{track['track']['title']} {track['track']['subtitle']}" for track in
            response.json()['tracks']['hits']]
