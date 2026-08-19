import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='FakeNewsDetector/1.0'
)

page = wiki.page("Artificial intelligence")

if page.exists():
    print(page.summary[:1000])