from pymongo import MongoClient

client = MongoClient("mongodb://root:root123@localhost:27017/test_db?authSource=admin")
print(client.list_database_names())
