import json
from youtube_extractor import get_audio_url, get_video_infos
from api_communication import save_transcript

def save_video_sentiments(audio_url):
    video_infos = get_video_infos(audio_url)
    audio_url = get_audio_url(video_infos)
    title = video_infos["title"]
    title = title.strip().replace(" ", "_")
    title = "data/" + title
    save_transcript(audio_url, title, sentiment_analysis=True)

if __name__ == "__main__":
    save_video_sentiments("https://www.youtube.com/watch?v=fu-ks-s9WMU")