import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_news(news_text, context):

    prompt = f"""
You are an expert Fake News Detection system.

User Claim:
{news_text}

Retrieved Evidence:
{context}

Tasks:

1. Determine whether the claim is REAL or FAKE.
2. Give a confidence percentage.
3. Explain your reasoning.

Return ONLY valid JSON:

{{
    "prediction": "",
    "confidence": "",
    "reason": ""
}}

Do not use markdown.
Do not use ```json.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content