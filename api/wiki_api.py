import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='FakeNewsDetector/1.0'
)


def get_wikipedia_context(query):

    page = wiki.page(query)

    if page.exists():

        return page.summary[:3000]

    return ""