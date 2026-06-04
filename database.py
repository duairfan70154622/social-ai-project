from pymongo import MongoClient

MONGO_URL = "mongodb+srv://70154622_db_user:jXcPs5Jhnrd7xM2u@cluster0.pcwxg0l.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URL)

print(client.list_database_names())