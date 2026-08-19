import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GUARDIAN_API_KEY")


def search_guardian(query):

    url = "https://content.guardianapis.com/search"

    params = {
        "q": query,
        "api-key": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        return data["response"]["results"]

    return []