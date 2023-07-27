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
    # save_video_sentiments("https://www.youtube.com/watch?v=QpW0cAG_-CY")

    with open ("data\Best_30_Seconds_In_The_History_of_Television_sentiments.json", "r") as f:
        data = json.load(f)
    
    positives = []
    negatives = []
    neutrals = []

    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        
        else:
            neutrals.append(text)


    n_pos = len(positives)
    n_neg = len(negatives)
    n_neut = len(neutrals)

    print("Num positives:", n_pos)
    print("Num negatives:", n_neg)
    print("Num neutrals:", n_neut)

    # ignore neutrals here
    r = n_pos / (n_pos + n_neg)
    print(f"Positive ratio: {r:3f}")