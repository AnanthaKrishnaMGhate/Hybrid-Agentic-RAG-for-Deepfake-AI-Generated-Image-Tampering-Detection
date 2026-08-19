import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WORLD_NEWS_API_KEY")


def search_world_news(query):

    url = "https://api.worldnewsapi.com/search-news"

    headers = {
        "x-api-key": API_KEY
    }

    params = {
        "text": query
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    if response.status_code == 200:

        data = response.json()

        return data.get("news", [])

    return []