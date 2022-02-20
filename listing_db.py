from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

# 전체 리스트 페이지
@app.route('/whole')
def whole():
    return render_template('full_list.html')

# 전체 리스트 페이지 API
# DB_gameList의 데이터를 불러와 출력하기
@app.route('/whole', methods=['GET'])
def show_gameList():
    games = list(db.mc10th.find({}, {'_id':False}))
    return jsonify({'all_games': games})

