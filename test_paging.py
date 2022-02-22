import os
from bson.objectid import ObjectId
import math
from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th




# 체크한 인원수가 4명이라면
# db의 데이터에서 최소 인원이 4보다 작고, 최대 인원이 4보다 큰 데이터를 찾아
# 해당 데이터를 출력

player_receive = 2
age_receive = [8,15]
genre_receive = '전략'
filtered_games = []


games = list(db.gameList.find({}, {'_id': False}))

# 인원수만 필터링
def filter_playerNum():
    for game in games:
        minNum_games = int(game['opt_minNum'])
        maxNum_games = int(game['opt_maxNum'])
        if minNum_games <= player_receive <= maxNum_games:
            filtered_games.append(game)
# 연령만 필터링
def filter_playerAge():
    for game in games:
        min_age = int(age_receive[0])
        max_age = int(age_receive[1])

        if min_age <= game['opt_age'] <= max_age:
            filtered_games.append(game)
# 장르만 필터링
def filter_playerGenre():
    find_genre = list(db.gameList.find({'opt_genre': genre_receive}, {'_id': False}))
    for game in find_genre:
        filtered_games.append(game)
# 인원수와 연령을 필터링
def filter_numAndAge():
    for game in games:
        minNum_games = int(game['opt_minNum'])
        maxNum_games = int(game['opt_maxNum'])
        min_age = int(age_receive[0])
        max_age = int(age_receive[1])
        if minNum_games <= player_receive <= maxNum_games and min_age <= game['opt_age'] <= max_age:
            filtered_games.append(game)
# 인원수와 장르를 필터링
def filter_numAndGenre():
    find_genre = list(db.gameList.find({'opt_genre': genre_receive}, {'_id': False}))
    for game in find_genre:
        minNum_games = int(game['opt_minNum'])
        maxNum_games = int(game['opt_maxNum'])
        if minNum_games <= player_receive <= maxNum_games:
            filtered_games.append(game)
# 연령과 장르를 필터링
def filter_ageAndGenre():
    find_genre = list(db.gameList.find({'opt_genre': genre_receive}, {'_id': False}))
    for game in find_genre:
        min_age = int(age_receive[0])
        max_age = int(age_receive[1])

        if min_age <= game['opt_age'] <= max_age:
            filtered_games.append(game)
# 모두를 필터링
def filter_all():
    find_genre = list(db.gameList.find({'opt_genre': genre_receive}, {'_id': False}))
    for game in find_genre:
        minNum_games = int(game['opt_minNum'])
        maxNum_games = int(game['opt_maxNum'])
        min_age = int(age_receive[0])
        max_age = int(age_receive[1])
        if minNum_games <= player_receive <= maxNum_games and min_age <= game['opt_age'] <= max_age:
            filtered_games.append(game)

# 인원수 선입력
if player_receive is not None:
    if age_receive is not None:
        if genre_receive is not None:
            filter_all()
        else:
            filter_numAndAge()
    elif genre_receive is not None:
        filter_numAndGenre()
    else:
        filter_playerNum()

# 연령 선입력
if age_receive is not None:
    if player_receive is not None:
        if genre_receive is not None:
            filter_all()
        else:
            filter_numAndAge()
    elif genre_receive is not None:
        filter_ageAndGenre()
    else:
        filter_playerAge()

# 장르 선입력
if genre_receive is not None:
    if player_receive is not None:
        if age_receive is not None:
            filter_all()
        else:
            filter_numAndGenre()
    elif age_receive is not None:
        filter_ageAndGenre()
    else:
        filter_playerGenre()


print(filtered_games)




# print(int(age_receive.split(',')[0]))
# print(player_receive, age_receive, genre_receive, time_receive)
# all_games = list(db.gameList.find({"opt_genre":genre_receive},{'_id':False}))


# min_age = int(age_receive.split(',')[0])
# max_age = int(age_receive.split(',')[1])
# for game in all_games:
#     if (int(game['opt_minNum']) <= int(player_receive) <= int(game['opt_maxNum'])) and (min_age <= int(game['opt_age']) <= max_age) :
#         filtered_games.append(game)

# return jsonify({'filtered_games': filtered_games})



