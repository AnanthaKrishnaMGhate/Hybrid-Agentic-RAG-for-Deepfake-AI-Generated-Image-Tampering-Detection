from newspaper import Article


def scrape_article(url):

    try:

        article = Article(url)

        article.download()

        article.parse()

        return article.text

    except Exception:

        return ""