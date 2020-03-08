# coding=utf-8
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Beer
num = [

]
name = [
    'PILSNER',
    'Munich Dunkel',
    'Belgian White',
    'Weizen',
    'Session I.P,A',
    'I.P.A India Pale Ale',
    'Orange Rye Gose',
    'Pale Ale',
    'Nugget Ale',
    'Honey Brown',
    'HampSeed Brown Ale',
    'Chocolate Stout'

]
sec = [
    'SRM 3 IBU 28  ABV 4.5%',
    'SRM 21 IBU 17  ABV 4.5%',
    'SRM 3 IBU 28  ABV 4.5%',
    'SRM 3 IBU 14  ABV 4.5%',
    'SRM 4 IBU 39  ABV 4.6%',
    'SRM 6 IBU 45  ABV 6.0%',
    'SRM 6.5 IBU 25  ABV 4.5%',
    'SRM 8 IBU 24  ABV 4.5%',
    'SRM 14 IBU 31  ABV 4.5%',
    'SRM 15 IBU 16  ABV 4.5%',
    'SRM 15 IBU 16  ABV 6.2%',
    'SRM 25 IBU 18  ABV 4.5%'

]

des = [
    '달큰한 빵맛과 비스킷, 구운 몰트의 풍미가 ​싸즈홉의 적당히 톡쏘는 풍미와 잘 어우러진 맥주',
    '독일 바이에른 지역의 클래식한 다크라거 스타일의 맥주로 ​몰트의 달콤한 풍미와 갓구운 빵의 로스트향이 잘 어우러진 맥주',
    '벨기에 호가든 지방의 전통주, 샤워몰트의 상큼함과 과일향이 어우러져 여름철 갈증해소에 최적화된 맥주',
    '독일 밀 몰트와 필스너 몰트를 사용 이스트로부터 우러나오는 바나나향과 클로브향의 조화가 일품',
    '달달한 멜론향에 시트러스향과 깔끔한 끝맛이 조화를 이루는 세션IPA',
    '홉의 강렬한 향과 쓴맛이 일품인 상면발효 맥주 2016 맥주대상 수상 맥주!',
    '독일 고제강에서 유래된 맥주로 더테이블에서 새롭게 오렌지향을 첨가. 상큼하며 기분좋은 신맛이 나는 맥주',
    '전통적인 미국 홉 풍미의 다양성을 대변하는 맥주 자몽, 소나무, 감귤류의 풍미를 느낄 수 있음',
    '너겟홉을 첨가하여 몰트에서 나는 갓 구운 빵, 비스킷 그리고 자색과일의 풍미가 균형을 이루는 맥주',
    '더테이블을 대표하는 맥주로서, 산뜻한 꿀향과 초컬릿향, 캬라멜향, 토피아향이 함께 어우러져 깊은 풍미를 만들어내는 맥주',
    '햄프씨드 (대마씨)를 첨가. 마일드캐러멜과 다크초콜릿, 고소한 견과류의 풍미를 즐길 수 있는 브라운 에일',
    '풍부한 바디감을 가지며 초콜릿 향과 캬라멜의 부드럽고 달콤한 피니쉬를 느낄 수 있는 Irish Stout'


]
for i in range(12):

        doc = {
            'num' : 3,
            'img' : 'https://postfiles.pstatic.net/20161007_39/thetable_beer_1475827334007VRRKm_JPEG/beers.jpg?type=w2',
            'brewery' : name[i],
            'sec' : sec[i],
            'des' : des[i]

        }

        db.beerList.insert_one(doc)

print(doc)