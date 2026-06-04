from fastapi import FastAPI
from database import db
from collections import Counter

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
@app.post("/add-tweet")
def add_tweet(text: str):

    try:
        collection.insert_one({
            "text": text,
            "sentiment": "ok"
        })

        return {"status": "saved"}

    except Exception as e:
        return {"error": str(e)}

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
import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)