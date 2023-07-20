import yt_dlp

ydl = yt_dlp.YoutubeDL()


def get_video_infos(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download=False
        )
    
    if "entries" in result:
        return result["entries"][0]
    return result

def get_audio_url(video_info):
    print(video_info)



if __name__ == "__main__":
    video_info = get_video_infos("https://www.youtube.com/watch?v=ob0p7G2QoHA")
    audio_url = get_audio_url(video_info)
    print(audio_url)