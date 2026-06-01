# youtube_service.py

from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

def get_comments(video_id):

    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )

    response = request.execute()

    for item in response["items"]:

        comment = item["snippet"] \
        ["topLevelComment"] \
        ["snippet"] \
        ["textDisplay"]

        comments.append(comment)

    return comments


