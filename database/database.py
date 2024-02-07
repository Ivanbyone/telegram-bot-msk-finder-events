from pymongo import MongoClient
from configs.config import DB_URL
from configs.config import DB_NAME

client = MongoClient(DB_URL)
database = client[DB_NAME]
user_collection = database.users


def registraton(id, username, fullname) -> None:
    user = {"user_id": id,
            "username": username,
            "fullname": fullname,
            "role": "user",
            "attempts": 5}
    
    user_collection.insert_one(user)


def validation(id) -> int:
    valid = list(user_collection.find({"user_id": id}))
    
    return len(valid)


def send_profile(id) -> dict:
    
    return dict(user_collection.find_one({"user_id": id}))
