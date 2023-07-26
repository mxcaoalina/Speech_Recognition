import yt_dlp #use yt_dlp instead of youtube_dl

ydl = yt_dlp.YoutubeDL()


def get_video_infos(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download=False # no need to download from youtube
        )
    
    if "entries" in result:
        return result["entries"][0]
    return result

# get video info
def get_audio_url(video_info):
    for f in video_info["formats"]:
        if f["ext"] == "m4a": # only need m4a file
            return f["url"]



if __name__ == "__main__":
    video_info = get_video_infos("https://www.youtube.com/watch?v=fu-ks-s9WMU")
    audio_url = get_audio_url(video_info)
    print(audio_url)