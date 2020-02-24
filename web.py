# coding=utf-8
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('beerTemplate.html')


@app.route('/new', methods=['POST'])
def new_post():
    score_receive = int(request.form['score_give'])
    brew_receive = request.form['brew_give']
    rank_receive = int(request.form['rank_give'])
    address_receive = request.form['address_give']

    db.brewerys.insert_one({'RateBeer-score': score_receive, 'brewery': brew_receive, 'rank': rank_receive, 'address': address_receive})

    return jsonify({'result': 'success'})


@app.route('/test', methods=['GET'])
def test_get():
    rank_receive = request.args.get('rank_give')
    rank_receive = int(rank_receive)
    brew_info = db.brewerys.find_one({'rank': rank_receive}, {'_id': 0})
    return jsonify({'result': 'success', 'info': brew_info})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
