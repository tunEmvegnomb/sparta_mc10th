from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
db = client.mc10th

games = list(db.gameList.find({}, {'_id': False}))

randNum1 = random.randrange(1,85)
randNum2 = random.randrange(1,85)
randNum3 = random.randrange(1,85)

# print(randNum1, randNum2, randNum3)
# randomGame = random.choice(games)
# name = randomGame['opt_name']

todayGame1 = db.gameList.find_one({'opt_rank':randNum1})['opt_img']
todayGame2 = db.gameList.find_one({'opt_rank':randNum2})['opt_img']
todayGame3 = db.gameList.find_one({'opt_rank':randNum3})['opt_img']

todaygames = [todayGame1,todayGame2,todayGame3]


a = 2
b = [3,10]
c = "가나다"

print(a, b, c)



# API 설계
# 데이터베이스에서 이미지와 랭크 값을 가져옴
# 랜덤함수 3번을 돌려 나온 숫자
# 그 숫자의 값을 랭크 값과 매치 시켜서
# 이미지를 뿌려줌

