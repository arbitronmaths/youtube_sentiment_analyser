# YouTube Sentiment Analyzer Chrome Extension

## Overview

YouTube Sentiment Analyzer is a Chrome Extension powered by Natural Language Processing (NLP) that analyzes the sentiment of comments on any YouTube video.

The extension extracts the current video's ID, sends it to a FastAPI backend, fetches comments using the YouTube Data API, performs sentiment analysis using a Hugging Face model, and displays the overall audience sentiment directly to the user.

---

## Features

* Analyze sentiment of YouTube comments
* Detect Positive, Neutral, and Negative comments
* FastAPI backend for processing
* Hugging Face NLP model integration
* Chrome Extension popup interface
* Real-time sentiment results
* REST API architecture

---

## Project Architecture

```text
YouTube Video
      ↓
Chrome Extension
      ↓
FastAPI Backend
      ↓
YouTube Data API
      ↓
Comment Collection
      ↓
Hugging Face Sentiment Model
      ↓
Sentiment Statistics
      ↓
Chrome Extension UI
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn
* YouTube Data API v3
* Hugging Face Transformers
* python-dotenv

### Frontend

* Chrome Extension (Manifest V3)
* HTML
* CSS
* JavaScript

### Machine Learning

* Hugging Face Transformers
* CardiffNLP Twitter RoBERTa Sentiment Model

## Future Improvements

* Sentiment trend charts
* Word cloud visualization
* Top positive comments
* Top negative comments
* In-page YouTube dashboard
* Multi-language sentiment analysis
* User sentiment history

