from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mc10th

# name = db.gameList.find_one({"opt_name":"할리갈리"})
# print(name)
#
# results = db.gameList.find({'opt_rank': {$lte:7}})
#
# for result in results:
#     print(result['opt_name'])

# 전체리스트
# for games in db.gameList.find():
#     print(games)

# 일부리스트
# for games in db.gameList.find({},{"_id":0, "opt_name":1, "opt_rank":1}):
#     print(games)

# 검색
# myquery = {"opt_name" : "우봉고"} #조건
# mygame = db.gameList.find(myquery) #검색
# for games in mygame: #반복문
#     print(games) #도출값

# 랜덤으로 숫자를 뽑아보자
# import random
# min = random.randint(1,8)
# print(min)

# 인원 검색리스트(랜덤)
# import random
# personnel = random.randint(1,8)  #1~8명까지 랜덤으로 한 숫자를 선택(인원 조건을 바꿔줌)
# myquery = {"opt_minNum" : personnel} #조건
# mygame = db.gameList.find(myquery) #검색
# for games1 in mygame: #반복문
#     print(games1) #결과값

# # 인원 전체리스트
# personnel = 2  # 2명인 인원 전체 리스트
# myquery = {"opt_minNum": personnel}  # 조건
# mygame = db.gameList.find(myquery,{'_id': False})  # 검색
# for games1 in mygame:  # 반복문
#     print(games1) #결과값

# 원하는 게임 연령리스트(랜덤)
# import random
# age = random.randint(3,10)  #3~10세까지 랜덤으로 한 숫자를 선택(나이 조건을 바꿔줌)
# myquery = {"opt_age" : age} #조건
# mygame = db.gameList.find(myquery,{'_id': False}) #검색
# for games2 in mygame: #반복문
#     print(games2) #결과값

# 원하는 게임 연령리스트
# age = 8  # 8세인 전체 리스트
# myquery = {"opt_age": age}  # 조건
# mygame = db.gameList.find(myquery,{'_id': False})  # 검색
# for games2 in mygame:  # 반복문
#   print(games2) #결과값

# 원하는 장르
# genre = "전략"  # 장르가 전략인 전체 리스트
# myquery = {"opt_genre": genre}  # 조건
# mygame = db.gameList.find(myquery,{'_id': False})  # 검색
# for games3 in mygame:  # 반복문
#   print(games3) #결과값

# 원하는 플레이타임, 장르, 연령, 인원으로 원하는 값 출력
time = 30  #플레이타임이 30분인 리스트
age = 8 #8세 연령리스트
personnel = 3 #최소인원이 3인 리스트
choice = {"opt_time": time, "opt_genre": "전략", "opt_age": age, "opt_minNum": personnel}  # 조건
choicegame = db.gameList.find(choice,{'_id': False})  # 검색
for games4 in choicegame:  # 반복문

    print([games4]) #결과값
    # print(games4['opt_name'])  # 이름 결과값
    #중복되는 이름에서 그 이름에 해당하는 딕셔너리 값을 뽑아오면 될 듯.

# 선택한 값 도출
# def find_keys(dict, val):
#   return list(key for key, value in dict.items() if value == val)