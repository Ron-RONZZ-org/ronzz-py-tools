# type: ignore
from ronzz_tool.youTube import download_youtube

# Download YouTube videos
youtube_urls = [
    "https://www.youtube.com/watch?v=exIDp2vlkmw",
    "https://www.youtube.com/watch?v=eKJclYAP2OI",
    "https://www.youtube.com/watch?v=9kDm7Kxncdk",
]
download_youtube(
    youtube_url_list=youtube_urls,
    output_path="/home/rongzhou/Musique",
    # output_path="/home/rongzhou/Documents/ronzz-linux-server-processing-sync/whisper-transskribo/election-municipale-fr",
    format="both",  # or "video", "both", "subtitle_only"
    preferred_audio_quality="192",
    subtitle=True,
)
