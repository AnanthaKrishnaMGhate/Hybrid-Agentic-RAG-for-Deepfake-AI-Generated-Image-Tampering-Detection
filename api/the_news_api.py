import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("THE_NEWS_API_KEY")


def search_the_news(query):

    url = "https://api.thenewsapi.com/v1/news/all"

    params = {
        "api_token": API_KEY,
        "search": query
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        return data.get("data", [])

    return []