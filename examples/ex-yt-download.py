# type: ignore
from ronzz_tool.youTube import download_youtube

# Download YouTube videos
youtube_urls = [
    "https://www.youtube.com/watch?v=G60OzaglxAQ",
    "https://www.youtube.com/watch?v=L_3KmTevD5o",
    "https://www.youtube.com/watch?v=c6rP-YP4c5I",
    "https://www.youtube.com/watch?v=uvdO0TJXjdc",
]
download_youtube(
    youtube_url_list=youtube_urls,
    output_path="/home/rongzhou/Musique",
    # output_path="/home/rongzhou/Documents/ronzz-linux-server-processing-sync/whisper-transskribo/election-municipale-fr",
    format="both",  # or "video", "both", "subtitle_only"
    preferred_audio_quality="192",
    subtitle=True,
)
