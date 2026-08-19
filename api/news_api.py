import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


def search_news(query, max_results=5):

    response = newsapi.get_everything(
        q=query,
        language="en",
        sort_by="relevancy",
        page_size=max_results
    )

    articles = []

    for article in response["articles"]:

        articles.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        })

    return articles