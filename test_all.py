print("\n========== TESTING APIs ==========\n")

# ----------------------------------
# NEWS API
# ----------------------------------
try:

    from api.news_api import search_news

    articles = search_news("Artificial Intelligence")

    print("✅ NewsAPI : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ NewsAPI :", e)


# ----------------------------------
# WIKIPEDIA
# ----------------------------------
try:

    from api.wiki_api import get_wikipedia_context

    get_wikipedia_context("Artificial Intelligence")

    print("✅ Wikipedia API : OK")

except Exception as e:

    print("❌ Wikipedia :", e)


# ----------------------------------
# GDELT
# ----------------------------------
try:

    from api.gdelt_api import search_gdelt

    articles = search_gdelt("Artificial Intelligence")

    print("✅ GDELT API : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ GDELT :", e)


# ----------------------------------
# GOOGLE SEARCH
# ----------------------------------
try:

    from api.google_search import google_search

    google_search("Artificial Intelligence")

    print("✅ Google Search API : OK")

except Exception as e:

    print("❌ Google Search :", e)


# ----------------------------------
# CURRENTS
# ----------------------------------
try:

    from api.currents_api import search_currents

    articles = search_currents("Artificial Intelligence")

    print("✅ Currents API : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ Currents API :", e)


# ----------------------------------
# MEDIASTACK
# ----------------------------------
try:

    from api.mediastack_api import search_mediastack

    articles = search_mediastack("India")

    print("✅ Mediastack API : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ Mediastack :", e)


# ----------------------------------
# ALPHA VANTAGE
# ----------------------------------
try:

    from api.alpha_news_api import search_alpha_news

    articles = search_alpha_news("Technology")

    print("✅ Alpha Vantage API : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ Alpha Vantage :", e)


# ----------------------------------
# NYT
# ----------------------------------
try:

    from api.nyt_api import search_nyt

    articles = search_nyt("AI")

    print("✅ New York Times API : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ New York Times :", e)


# ----------------------------------
# GUARDIAN
# ----------------------------------
try:

    from api.guardian_api import search_guardian

    articles = search_guardian("AI")

    print("✅ Guardian API : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ Guardian API :", e)


# ----------------------------------
# THE NEWS API
# ----------------------------------
try:

    from api.the_news_api import search_the_news

    articles = search_the_news("AI")

    print("✅ TheNewsAPI : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ TheNewsAPI :", e)


# ----------------------------------
# WORLD NEWS API
# ----------------------------------
try:

    from api.world_news_api import search_world_news

    articles = search_world_news("AI")

    print("✅ World News API : OK")
    print("Articles:", len(articles))

except Exception as e:

    print("❌ World News API :", e)


# ----------------------------------
# RSS LINKS
# ----------------------------------
try:

    from api.rss_feeds import fetch_rss_links

    links = fetch_rss_links()

    print("✅ RSS Feeds : OK")
    print("Links:", len(links))

except Exception as e:

    print("❌ RSS Feeds :", e)


# ----------------------------------
# CHANNEL SCRAPER
# ----------------------------------
try:

    from api.channel_scraper import scrape_channels

    articles = scrape_channels()

    print("✅ Channel Scraper : OK")
    print("Articles Found:", len(articles))

except Exception as e:

    print("❌ Channel Scraper :", e)


# ----------------------------------
# FAISS
# ----------------------------------
try:

    from rag.retriever import retrieve_documents

    retrieve_documents("AI")

    print("✅ FAISS Retriever : OK")

except Exception as e:

    print("❌ FAISS :", e)


# ----------------------------------
# GROQ
# ----------------------------------
try:

    from llm.groq_llm import analyze_news

    analyze_news(
        "NASA confirms aliens landed in India",
        "No evidence found."
    )

    print("✅ Groq API : OK")

except Exception as e:

    print("❌ Groq :", e)


print("\n========== DONE ==========\n")