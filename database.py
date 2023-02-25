from pymongo import MongoClient

client = MongoClient('')
db = client.pythondb

def registered(name):
    
    if( db.discord_id.find({ "discord_user_data": { "discord_id": name } }).count() != 0 ):
        return -1 # already registered
    
    user_data = {
        "discord_id": "-1",
        "money": "0",
        "last_time": "-1",
    }
    
    user_data["discord_id"] = name
    db["discord_user_data"].insert_one(user_data)
    print(1)
    return 1 # registered completed!