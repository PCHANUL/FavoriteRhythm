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
    result = list(db.brewerys.find({},{'_id':0}))

    return jsonify({'result': 'success', 'brewerys':result})





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
