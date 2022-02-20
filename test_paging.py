import mongo as mongo
import os
from bson.objectid import ObjectId
import math
from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)



# 전체 리스트 페이지 API
# 페이지네이션 기능
# 데이터를 한 페이지당 15 개로 제한하고
# 다음 데이터부터 페이지를 넘어가면서 출력
# 현재 84개의 데이터 = 6개의 페이지 생성
@app.route("/whole/page", methods=['GET'])
def list_page():
    ## ajax에서 url을 넘겨준 키값을 통해 현재 게시물 페이지 넘버 확인가능 ##
    page = request.args.get('page', 1, type=int)
    ## 한 페이지당 15개의 게시물을 보여줌 ##
    limit = 15
    ##skip(배열 또는 리스트 시작숫자)함수 mongoDB 함수 시작부분을 return 시작전 data는 버려짐 ##
    ##limit(숫자) 제한된 개수를 return해줌 ##
    game_list = db.gameList.find({}).skip((page - 1) * limit).limit(limit)

    ## db에 저장된 총 게시물의 개수
    tot_count = db.gameList.find({}).count()
    last_page_num = math.ceil(tot_count / limit)

    ## Object형식을 json에 필요한 str형식으로 바꿔주기 위한 decode
    results = []
    for document in game_list:
        document['_id'] = str(document['_id'])
        results.append(document)

    return jsonify({'list': results,
                    'limit': limit,
                    'page': page,
                    'last_page_num': last_page_num})