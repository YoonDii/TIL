import json 
from pprint import pprint # 예쁘게 출력해줌
# 파일을 열고, 

f = open('stocks.json', 'r', encoding='utf-8')
# JSON을 파이썬 객체 형식으로 변환한다.
kospi = json.load(f)
samsung = kospi['stocks'][0]
# print(samsung, type(samsung))

# stockName 정보랑, closePrice 정보만 가진 딕셔너리를 만들자
result = {
    'stockName': samsung.get('stockName'),
    'closePrice': samsung.get('closePrice') #파이썬에선 그냥 이렇게 쓰는게 편하고 좋다!
}

print(result)