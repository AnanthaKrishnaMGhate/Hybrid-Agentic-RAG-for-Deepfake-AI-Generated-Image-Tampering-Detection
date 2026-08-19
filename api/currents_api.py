import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CURRENTS_API_KEY")


def search_currents(query):

    url = "https://api.currentsapi.services/v1/search"

    params = {
        "keywords": query,
        "language": "en",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        return data.get("news", [])

    return []