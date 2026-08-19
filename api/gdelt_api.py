import requests
from requests.exceptions import RequestException


def search_gdelt(query):

    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {
        "query": query,
        "mode": "ArtList",
        "maxrecords": 5,
        "format": "json",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            return []

        if isinstance(data, dict):
            return data.get("articles", [])
    except RequestException:
        pass

    return []
