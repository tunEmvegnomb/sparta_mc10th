from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

games = list(db.gameList.find({}, {'_id': False}))
print(games)
# for n in games:
#     name = n['opt_name']
#     print(name)


