from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sentiment_service import query
from youtube_service import get_comments

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/analyze/{video_id}")
def analyze(video_id: str):
    comments = get_comments(video_id)
    sentiments = query(comments)
    return {"sentiments": sentiments}