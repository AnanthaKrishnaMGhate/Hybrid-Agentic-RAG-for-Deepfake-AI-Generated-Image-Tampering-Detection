from rag.retriever import retrieve_documents

# Existing APIs
from api.news_api import search_news
from api.wiki_api import get_wikipedia_context
from api.gdelt_api import search_gdelt
from api.currents_api import search_currents
from api.mediastack_api import search_mediastack
from api.alpha_news_api import search_alpha_news
from api.nyt_api import search_nyt

# New APIs
from api.guardian_api import search_guardian
from api.the_news_api import search_the_news
from api.world_news_api import search_world_news

# RSS + Scraping
from api.rss_feeds import fetch_rss_links
from api.article_scraper import scrape_article

# LLM
from llm.groq_llm import analyze_news


def run_rag(news_query):

    # =====================================
    # FAISS RETRIEVAL
    # =====================================

    local_docs = retrieve_documents(
        news_query,
        top_k=10
    )

    dataset_context = "\n".join(local_docs)

    # =====================================
    # WIKIPEDIA
    # =====================================

    wiki_context = get_wikipedia_context(news_query)

    # =====================================
    # NEWS API
    # =====================================

    news_context = ""

    try:

        articles = search_news(news_query)

        for article in articles:

            title = str(article.get("title", ""))
            description = str(article.get("description", ""))

            news_context += title + "\n"
            news_context += description + "\n\n"

    except:
        pass

    # =====================================
    # GDELT
    # =====================================

    gdelt_context = ""

    try:

        articles = search_gdelt(news_query)

        for article in articles[:5]:

            gdelt_context += (
                str(article.get("title", "")) + "\n"
            )

    except:
        pass

    # =====================================
    # CURRENTS
    # =====================================

    currents_context = ""

    try:

        articles = search_currents(news_query)

        for article in articles[:5]:

            currents_context += (
                str(article.get("title", "")) + "\n"
            )

    except:
        pass

    # =====================================
    # MEDIASTACK
    # =====================================

    mediastack_context = ""

    try:

        articles = search_mediastack(news_query)

        for article in articles[:5]:

            mediastack_context += (
                str(article.get("title", "")) + "\n"
            )

    except:
        pass

    # =====================================
    # ALPHA VANTAGE
    # =====================================

    alpha_context = ""

    try:

        articles = search_alpha_news(news_query)

        for article in articles[:5]:

            alpha_context += (
                str(article.get("title", "")) + "\n"
            )

    except:
        pass

    # =====================================
    # NEW YORK TIMES
    # =====================================

    nyt_context = ""

    try:

        articles = search_nyt(news_query)

        for article in articles[:5]:

            nyt_context += (
                article["headline"]["main"] + "\n"
            )

    except:
        pass

    # =====================================
    # GUARDIAN API
    # =====================================

    guardian_context = ""

    try:

        articles = search_guardian(news_query)

        for article in articles[:5]:

            guardian_context += (
                article["webTitle"] + "\n"
            )

    except:
        pass

    # =====================================
    # THE NEWS API
    # =====================================

    the_news_context = ""

    try:

        articles = search_the_news(news_query)

        for article in articles[:5]:

            the_news_context += (
                str(article.get("title", "")) + "\n"
            )

    except:
        pass

    # =====================================
    # WORLD NEWS API
    # =====================================

    world_news_context = ""

    try:

        articles = search_world_news(news_query)

        for article in articles[:5]:

            world_news_context += (
                str(article.get("title", "")) + "\n"
            )

    except:
        pass

    # =====================================
    # RSS + ARTICLE SCRAPING
    # =====================================

    rss_context = ""

    try:

        rss_links = fetch_rss_links()

        for url in rss_links[:10]:

            article_text = scrape_article(url)

            rss_context += article_text + "\n\n"

    except:
        pass

    # =====================================
    # FINAL CONTEXT
    # =====================================

    final_context = f"""

========== FAISS DATASET ==========
{dataset_context}

========== WIKIPEDIA ==========
{wiki_context}

========== NEWS API ==========
{news_context}

========== GDELT ==========
{gdelt_context}

========== CURRENTS ==========
{currents_context}

========== MEDIASTACK ==========
{mediastack_context}

========== ALPHA VANTAGE ==========
{alpha_context}

========== NEW YORK TIMES ==========
{nyt_context}

========== GUARDIAN ==========
{guardian_context}

========== THE NEWS API ==========
{the_news_context}

========== WORLD NEWS API ==========
{world_news_context}

========== RSS SCRAPED ARTICLES ==========
{rss_context}

"""

    # Remove duplicate lines
    final_context = "\n".join(
        list(set(final_context.splitlines()))
    )

    # Limit size
    final_context = final_context[:20000]

    # =====================================
    # GROQ
    # =====================================

    response = analyze_news(
        news_query,
        final_context
    )

    return response