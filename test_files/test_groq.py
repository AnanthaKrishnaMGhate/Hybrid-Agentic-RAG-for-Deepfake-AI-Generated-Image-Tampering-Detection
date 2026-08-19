from llm.groq_llm import analyze_news

response = analyze_news(
    "NASA confirms aliens landed in New York",
    "No trusted source supports this claim."
)

print(response)