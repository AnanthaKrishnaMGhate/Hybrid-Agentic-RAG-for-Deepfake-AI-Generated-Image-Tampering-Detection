import newspaper

from api.news_sources import NEWS_SOURCES


def scrape_channels():

    articles_data = []

    for source, url in NEWS_SOURCES.items():

        try:

            paper = newspaper.build(url)

            for article in paper.articles[:10]:

                try:

                    article.download()
                    article.parse()

                    articles_data.append({

                        "source": source,
                        "title": article.title,
                        "text": article.text

                    })

                except:
                    pass

        except:
            pass

    return articles_data