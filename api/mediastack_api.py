import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MEDIASTACK_API_KEY")


def search_mediastack(query):

    url = "http://api.mediastack.com/v1/news"

    params = {
        "access_key": API_KEY,
        "keywords": query,
        "languages": "en",
        "limit": 5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        return data.get("data", [])

    return []