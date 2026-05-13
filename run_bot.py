from openai import OpenAI
from dotenv import load_dotenv
from moviepy import (
    VideoFileClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips
)
import os
import random

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Trending topics
topics = [
    "Best AI side hustles",
    "How to make money with AI",
    "Top AI tools in 2026",
    "AI business ideas",
    "How AI is changing jobs"
]

# Pick topic
topic = random.choice(topics)

print(f"Selected Topic: {topic}")

# Generate script
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "Create a short engaging YouTube Shorts script."
        },
        {
            "role": "user",
            "content": f"Create a viral short script about {topic}"
        }
    ]
)

script = response.choices[0].message.content

print("\nGenerated Script:\n")
print(script)

# Generate voiceover
voice = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input=script
)

voice.stream_to_file("voiceover.mp3")

print("Voiceover created.")

# Load background video
video = VideoFileClip("short.MOV")

# Load audio
audio = AudioFileClip("voiceover.mp3")

# Match duration
if video.duration < audio.duration:
    loops_needed = int(audio.duration // video.duration) + 1
    clips = [video] * loops_needed
    from moviepy import concatenate_videoclips
    video = concatenate_videoclips(clips)

video = video.subclipped(0, audio.duration)

# Add audio
video = video.with_audio(audio)

# Add captions
caption = TextClip(
    text=topic,
    font_size=70,
    color="white",
    size=video.size,
    method="caption"
)

caption = caption.with_position("center").with_duration(audio.duration)

# Combine video
final_video = CompositeVideoClip(
    [video, caption]
).with_duration(audio.duration)

# Export final video
final_video.write_videofile(
    "final_short.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

print("Final short video created.")