from pymongo import MongoClient

client = MongoClient('')
db = client.pythondb

def adding_money(name,val):
    if( repeat_register(name) == 1 ): # not register yet
        return
    
    now_money = query_money(name) 
    query_data = { 'discord_id': name }
    new_data = {'$set': { 'money': now_money+val }  }

    db["discord_user_data"].update_one(query_data,new_data)


def query_money(name):
    if( repeat_register(name) == 1 ):
        return -1 # not register yet

    for i in db["discord_user_data"]:
        if( i["discord_id"] == id ):
            return i["money"]

def repeat_register(id):

    ok = 1

    for i in db["discord_user_data"]:
        if( i['discord_id'] == id ):
            ok = 0
    
    return ok

def registered(name): 

    if( repeat_register(name) == 0 ):
        return -1 # already registered
    
    user_data = {
        "discord_id": "-1",
        "money": "0",
        "last_time": "-1",
    }
    
    user_data["discord_id"] = name
    db["discord_user_data"].insert_one(user_data)
    return 1 # registered completed!