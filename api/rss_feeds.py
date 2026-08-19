import feedparser

RSS_URLS = [

    "https://feeds.bbci.co.uk/news/rss.xml",

    "https://feeds.reuters.com/reuters/topNews",

    "https://feeds.feedburner.com/ndtvnews-top-stories",

    "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",

    "https://www.thehindu.com/news/feeder/default.rss"

]


def fetch_rss_links():

    links = []

    for url in RSS_URLS:

        try:

            feed = feedparser.parse(url)

            for entry in feed.entries[:5]:

                links.append(entry.link)

        except:

            pass

    return links