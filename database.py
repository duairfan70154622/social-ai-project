from pymongo import MongoClient

MONGO_URL = "mongodb+srv://testuser:Test12345@cluster0.pcwxg0l.mongodb.net/social_ai?retryWrites=true&w=majority"

client = MongoClient(MONGO_URL)

db = client["social_ai"]
collection = db["tweets"]