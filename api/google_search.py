import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")


def google_search(query, num_results=5):

    service = build(
        "customsearch",
        "v1",
        developerKey=GOOGLE_API_KEY
    )

    result = service.cse().list(
        q=query,
        cx=SEARCH_ENGINE_ID,
        num=num_results
    ).execute()

    links = []

    if "items" in result:
        for item in result["items"]:
            links.append(item["link"])

    return links