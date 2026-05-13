from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# AI script text
script = """
AI is changing the world faster than ever.
From content creation to automation,
these tools are helping people make money online,
save time, and grow businesses.
"""

# Generate voice
response = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input=script
)

# Save audio
response.stream_to_file("voiceover.mp3")

print("Voiceover saved as voiceover.mp3")