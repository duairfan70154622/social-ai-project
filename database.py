from pymongo import MongoClient

MONGO_URL = "mongodb+srv://social_user:cHXCJiN92KLeoIkX@cluster0.pcwxg0l.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

db = client["social_ai"]