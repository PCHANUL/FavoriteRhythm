# coding=utf-8
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Beer

c = ''
a = 1
b = [


    '3.43',
    '3.56',
    '3.51',
    '3.85',
    '3.47',
    '3.66',
    '3.66',
    '3.35',
    '4.04',
    '3.51',
    '3.61',
    '3.46',
    '3.35',
    '3.35',
    '3.56',
    '3.51',
    '3.26',
    '3.39',
    '3.83',
    'none',
    '3.37',
    '3.48',
    '3.51',
    '3.12',
    '3.51',
    'none',
    'none',
    'none',
    '3.16',
    '3.50',
    '3.35',
    'none',
    '3.34',
    '3.52',
    '3.39'



]
for i in range(35):
    db.brewerys.update_one({'rank':a}, {'$set':{'score2':b[i]}})
    a += 1



brewery = db.brewerys.find_one({'rank':1})
print(brewery)