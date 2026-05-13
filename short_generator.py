from moviepy import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip

# Load background video
video = VideoFileClip("short.MOV")

# Load AI Voiceover
audio = AudioFileClip("voiceover.mp3")

# Match Video Length Audio
video = video.subclipped(0, audio.duration)

# Add Audio to Video
video = video.with_audio(audio)

# Create Caption Text
caption = TextClip(
    text="AI is changing the future!",
    font_size=70,
    color="white",
    size=video.size,
    method="caption"
)
caption = caption.with_position("center").with_duration(audio.duration)
# Combine Video and Caption
final_video = CompositeVideoClip([video, caption]).with_duration(audio.duration)

# Export final video
final_video.write_videofile(
    "final_short.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

print("Short video created: final_short.mp4")
