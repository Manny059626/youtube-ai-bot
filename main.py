from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ask user for topic
topic = input("Enter a YouTube video topic: ")

# Generate script
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a professional YouTube script writer."
        },
        {
            "role": "user",
            "content": f"Write a YouTube video script about {topic}"
        }
    ]
)

# Get AI response
script = response.choices[0].message.content

# Print script
print("\nGenerated Script:\n")
print(script)

# Save to file
with open("youtube_script.txt", "w", encoding="utf-8") as file:
    file.write(script)

print("\nScript saved to youtube_script.txt")