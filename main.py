from fastapi import FastAPI
from collections import Counter
from database import db

app = FastAPI()

collection = db["tweets"]

# HOME
@app.get("/")
def home():
    return {"message": "AI Social Media System Running"}

# ADD TWEET
@app.post("/add-tweet")
def add_tweet(text: str):

    if "love" in text.lower():
        sentiment = "Positive 😃"
    elif "hate" in text.lower():
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    collection.insert_one({
        "text": text,
        "sentiment": sentiment
    })

    return {
        "text": text,
        "sentiment": sentiment,
        "status": "saved"
    }

# GET TWEETS
@app.get("/tweets")
def get_tweets():

    data = list(collection.find({}, {"_id": 0}))

    return {
        "count": len(data),
        "tweets": data
    }

# TRENDS
@app.get("/trends")
def trends():

    stopwords = {"is", "the", "i", "a", "an", "and", "to", "of", "in"}

    data = collection.find()

    words = []

    for item in data:
        text = item.get("text", "")
        for w in text.lower().split():
            if w not in stopwords:
                words.append(w)

    top_words = Counter(words).most_common(5)

    return {
        "trends": top_words
    }