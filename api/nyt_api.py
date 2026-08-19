import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NYT_API_KEY")


def search_nyt(query):

    url = (
        "https://api.nytimes.com/svc/search/v2/articlesearch.json"
        f"?q={query}"
        f"&api-key={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        docs = data["response"]["docs"]

        return docs

    return []