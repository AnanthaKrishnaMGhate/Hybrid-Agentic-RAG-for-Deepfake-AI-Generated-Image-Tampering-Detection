from newspaper import Article


def scrape_article(url):

    try:

        article = Article(url)

        article.download()

        article.parse()

        return {

            "title": article.title,
            "text": article.text,
            "authors": article.authors,
            "publish_date": article.publish_date

        }

    except Exception as e:

        print(e)

        return None