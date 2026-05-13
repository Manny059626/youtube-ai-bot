from openai import OpenAI
from dotenv import load_dotenv
import os
import random

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Trending topics list
trending_topics = [
    "Best AI side hustles in 2026",
    "How to make money using ChatGPT",
    "Best AI tools for students",
    "Top passive income apps",
    "AI business ideas for beginners",
    "How creators are using AI",
    "Best productivity hacks with AI",
    "Faceless YouTube channel ideas",
    "How to grow on YouTube Shorts",
    "TikTok automation strategies",
    "AI video generation tools",
    "Best online business ideas",
    "How to automate content creation",
    "Top AI apps going viral",
    "Future tech trends in 2026"
]

# Pick random trending topic
topic = random.choice(trending_topics)

print(f"\nTrending Topic Selected: {topic}\n")

# Generate content
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": """
            You are a viral YouTube strategist.

            Generate:
            1. Viral YouTube title
            2. SEO description
            3. 10 hashtags
            4. Thumbnail ideas
            5. Engaging YouTube script
            """
        },
        {
            "role": "user",
            "content": f"Create viral YouTube content about: {topic}"
        }
    ]
)


# Get content
content = response.choices[0].message.content

# Print content
print(content)

# Save content
with open("youtube_content.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("\nContent saved to youtube_content.txt")