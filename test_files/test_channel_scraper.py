from api.channel_scraper import scrape_channels

articles = scrape_channels()

print("\n========== CHANNEL SCRAPER TEST ==========\n")

print("Articles Found:", len(articles))

for article in articles[:10]:

    print("Source :", article["source"])
    print("Title  :", article["title"])

    # Print first 200 characters only
    text = article["text"][:200]

    print("Preview:", text)

    print("-" * 80)

print("\n========== DONE ==========\n")