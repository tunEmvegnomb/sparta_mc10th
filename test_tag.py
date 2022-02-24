from pymongo import MongoClient

import random

import math
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th


# API 설계
# 태그 데이터
    # 태그는 약 10~20 여 종류로 되어 있는 문자열로
    # 사용자가 여러 개 중 하나의 태그를 선택하면
    # 프론트에서 값을 선언하고
    # 백에서 give 값으로 받아
    # 태그 값과 비교하여 일치하는 데이터를 필터

    # 태그 1, 2, 3의 옵션에 각각 나눠서 들어가 있다.
    # 태그 1, 2, 3의 데이터가 따로 나올텐데 하나로 묶여서 나올 수 있어야함

games = list(db.gameList.find({},{'_id': False}))
tag_receive = '순발력'
for game in games:
    tag_1 = game['opt_tag1']
    tag_2 = game['opt_tag2']
    tag_3 = game['opt_tag3']
    if tag_1 == tag_receive or tag_2 == tag_receive or tag_3 == tag_receive:




