import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")


def search_alpha_news(query):

    url = (
        "https://www.alphavantage.co/query"
        "?function=NEWS_SENTIMENT"
        f"&topics={query}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        return data.get("feed", [])

    return []