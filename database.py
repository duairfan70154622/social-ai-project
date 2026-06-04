<<<<<<< HEAD
from pymongo import MongoClient

MONGO_URL = "mongodb+srv://testuser:Test12345@cluster0.pcwxg0l.mongodb.net/social_ai?retryWrites=true&w=majority"

client = MongoClient(MONGO_URL)

db = client["social_ai"]
=======
from pymongo import MongoClient

MONGO_URL = "mongodb+srv://testuser:Test12345@cluster0.pcwxg0l.mongodb.net/social_ai?retryWrites=true&w=majority"

client = MongoClient(MONGO_URL)

db = client["social_ai"]
>>>>>>> 9e3400cb1b58be65b665a86e42a4a38c67fc3f20
collection = db["tweets"]