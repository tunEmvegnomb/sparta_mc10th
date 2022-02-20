from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

import random

import math
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def home():
    return render_template('index.html')

# 메인 페이지 API
# API 설계
    # 데이터베이스에서 이미지와 랭크 값을 가져옴
    # 랜덤함수 3번을 돌려 나온 숫자
    # 그 숫자의 값을 랭크 값과 매치 시켜서
    # 이미지를 뿌려줌
@app.route('/rand', methods=['GET'])
def today_random():

    randnum1 = random.randrange(1, 85)
    randnum2 = random.randrange(1, 85)
    randnum3 = random.randrange(1, 85)

    todaygame1 = db.gameList.find_one({'opt_rank': randnum1})['opt_img']
    todaygame2 = db.gameList.find_one({'opt_rank': randnum2})['opt_img']
    todaygame3 = db.gameList.find_one({'opt_rank': randnum3})['opt_img']

    todaygames = [todaygame1, todaygame2, todaygame3]
    return jsonify('todaygames', todaygames)



# 질문 페이지
@app.route('/survey')
def survey():
    return render_template('question.html')

# 질문 페이지 API
# 질답에 체크한 데이터를 DB_survey에 저장하고
# DB_gameList와 비교하여
# 일치하는 데이터들을 뽑아내는 기능
@app.route('/survey', methods=['POST'])
def search_survey():
    num_receive = request.form['num_give']
    age_receive = request.form['age_give']
    genre_receive = request.form['genre_give']
    time_receive = request.form['time_give']

    doc = {
        'sur_num': num_receive,
        'sur_age': age_receive,
        'sur_genre': genre_receive,
        'sur_time': time_receive
    }
    db.survey.insert_one(doc)
    return jsonify({'msg': '저장되었습니다!'})

# 결과 페이지
@app.route('/result')
def result():
    return render_template('result.html')

# 결과값 보내주기
@app.route('/resultData', methods=['POST'])
def output_result():
    player_receive = request.form['player_give']
    age_receive = request.form['age_give']
    genre_receive = request.form['genre_give']
    time_receive = request.form['time_give']
    # print(int(age_receive.split(',')[0]))
    # print(player_receive, age_receive, genre_receive, time_receive)
    all_games = list(db.mc10th.find({"opt_genre":genre_receive},{'_id':False}))
    filtered_games = []
    min_age = int(age_receive.split(',')[0])
    max_age = int(age_receive.split(',')[1])
    min_time = int(time_receive.split(',')[0])
    max_time = int(time_receive.split(',')[1]) 
    for game in all_games:
        if (int(game['opt_minNum']) <= int(player_receive) <= int(game['opt_maxNum'])) and (min_age <= int(game['opt_age']) <= max_age) and ( min_time <= int(game['opt_time']) <= max_time ) :
            filtered_games.append(game)
    return jsonify({'filtered_games': filtered_games})

# 전체 리스트 페이지
@app.route('/whole')
def whole():
    return render_template('full_list.html')

# 전체 리스트 페이지 API
# DB_gameList의 데이터를 불러와 출력하기
@app.route('/whole/list', methods=['GET'])
def show_gameList():
    games = list(db.gameList.find({}, {'_id': False}))

    return jsonify({'all_games': games})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)