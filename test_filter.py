
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.mc10th

genre_receive = request.form['num_give']
genre = '가족'
filtered_game = list(db.gameList.find({'opt_genre': genre}, {'_id': False}))
for a in filtered_game:
    b = a['opt_name']
    print(b)