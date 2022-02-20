from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

#client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

#메인 페이지
@app.route('/')
def home():
    return render_template('index.html')

#질문 페이지
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

    # 원하는 플레이타임, 장르, 연령, 인원으로 원하는 값 출력
    time = time_receive  # 플레이타임리스트
    genre = genre_receive # 장르리스트
    age = age_receive  # 연령리스트
    num = num_receive  # 최소인원리스트
    choice = {"opt_time": time, "opt_genre": genre, "opt_age": age, "opt_minNum": num}  # 조건
    choicegame = db.gameList.find(choice, {'_id': False})  # 검색
    for mygames in choicegame:  # 반복문
        print(mygames) # 필터링 할 값 받아옴. 한 개의 값만 받아오는게 안됨.
    return jsonify({mygames}) #코드 작성하다가 잘 모르겠음.

#질문페이지 게임보기 API
@app.route('/survey', methods=['GET'])
def view_games():
    games = list(db.gameList.find({}, {'_id': False}))
    return jsonify({games})

# 결과 페이지
# @app.route('/result')
# def result():
#     return render_template('result.html')
#
# 전체 리스트 페이지
@app.route('/whole')
def whole():
    return render_template('full_list.html')
#
# # 전체 리스트 페이지 API
# # DB_gameList의 데이터를 불러와 출력하기
# @app.route('/whole', methods=['GET'])
# def show_gameList():
#     games = list(db.mc10th.find({}, {'_id':False}))
#     return jsonify({'all_games': games})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)