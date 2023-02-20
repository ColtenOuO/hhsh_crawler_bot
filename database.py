from pymongo import MongoClient

client = MongoClient('mongodb+srv://<username>:<password>@coltenbot.2y7nwf9.mongodb.net/test')

db = client.pythondb

test = {
    "name": "Colten",
    "money": "0",
}

u = db["name"]
x = u.insert_one(test)
print(x)
