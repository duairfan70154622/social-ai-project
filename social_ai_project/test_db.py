from database import db

# test collection
collection = db["tweets"]

# sample data insert
collection.insert_one({
    "text": "I love AI",
    "sentiment": "positive"
})

print("Data inserted successfully")