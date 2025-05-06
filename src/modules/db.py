from pymongo import MongoClient

from src.modules.env import Env

db = MongoClient(
    Env.MONGODB_URI,
    username=Env.MONGODB_USER,
    password=Env.MONGODB_PASSWORD,
    authSource="admin",
    port=Env.MONGODB_PORT,
)[Env.MONGODB_DB]

# db["users"].insert_one({"name": "John Doe", "email": "duong"})
# d = db["users"].find_one({"name": "John Doe"})
