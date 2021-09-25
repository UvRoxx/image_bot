import random
from pprint import pprint

import requests


def get_porn(query, content):
    URL = f"https://www.eporner.com/api/v2/video/search/?query={query}&per_page=10&page=2&thumbsize=big&order=top-weekly&gay=0"
    response = requests.get(URL)
    response = response.json()
    if content == 'video':
        vid = random.randint(0, 9)
        return response['videos'][vid]['url']
    else:
        vid = random.randint(0, 9)
        return response['videos'][vid]['default_thumb']['src']
