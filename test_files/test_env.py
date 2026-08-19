from dotenv import load_dotenv
import os

load_dotenv()

print("\n===== ENV VARIABLES =====\n")

print("Groq Key:", os.getenv("GROQ_API_KEY"))
print("NewsAPI Key:", os.getenv("NEWS_API_KEY"))
print("Google Key:", os.getenv("GOOGLE_API_KEY"))
print("Wikipedia: No API Key Required")