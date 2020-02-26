# coding=utf-8
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Beer


a = 1
b = [
    'Mon-Fri 16:00-01:00 Sat-Sun 12:00-01:00',
    'Brewshop Hours: Tue-Sun, 3-10:00 PM Basement Hours: Tue-Sun, 5:00 PM-2:00 AM',
    '',
    'T - F 5:00 - 12:00 S - S 3 - 11:00',
    '',
    '11:30~24:00',
    '11:30~24:00',
    '5:00 PM-1:00 AM',
    '5pm - 1am Closed Tuesdays',
    '2pm - 2am',
    '',
    'M - F 5:00 - 11:30 S - S 12:00 - 12:00',
    'Mon-Fri 5:00 PM-1:00 AM Sat 12:00 PM-1:00 AM Sun 12:00 PM-11:00 PM',
    '11:00 AM-1:00 AM',
    'Mon-Thu 6P.M. - 1A.M. / Fri 5P.M. - 1A.M. / Sat 3P.M. - 11P.M. / Sun Off',
    'M - F 4:00 - 12:00 S - S 12:00 - 12:00',
    '',
    'Friday, Saturday, Sunday',
    'M-F 6:00PM - 12:00AM S 1:00PM - 12:00 AM S 1:00PM - 11:00PM',
    '',
    '6pm - 1am Closed Monday',
    '13:00 - 23:00',
    '',
    '5:00 PM-2:00 AM',
    '',
    '',
    '6:00 PM-1:00 AM',
    '',
    'Sun-Sat 11:00 AM-2:00 AM',
    '',
    'Mon-Thu 12:00 PM-1:00 AM, Fri,Sat 12:00 PM-2:00 AM, Sun 12:00 PM-11:00 PM',
    '',
    '10:00 AM ~ 3:00 AM',
    'Mon-Thu: 6:00 PM-3:00 AM Fri-Sat: 3:00 PM-5:00 AM Sun: 3:00 PM-2:00 AM',
    '11:30~24:00'




]
for i in range(35):
    db.brewerys.update_one({'rank':a}, {'$set':{'time':b[i]}})
    a += 1



brewery = db.brewerys.find_one({'rank':1})
print(brewery)