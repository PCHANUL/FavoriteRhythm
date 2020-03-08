# coding=utf-8
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.Beer


@app.route('/')
def home():
    return render_template('beerTemplate.html')


@app.route('/post', methods=['GET'])
def listing():
    result = list(db.brewerys.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'brewerys': result})


@app.route('/list', methods=['GET'])
def beer():


    # rank_give로 클라이언트가 준 rank을 가져오기
    rank_receive = request.args.get('rank_give')

    # rank_receive를 숫자로 만들어주기 (db엔 숫자로 저장되어있으니까!)
    rank_receive = int(rank_receive)

    # rank의 값이 받은 rank와 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    result = list(db.beerList.find({'num': rank_receive}, {'_id': 0}))


    # info라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'beerList': result})



@app.route('/beerList')
def beerList():
    return render_template('beerList.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
