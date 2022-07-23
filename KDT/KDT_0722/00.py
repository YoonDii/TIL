#아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오. 

import requests  #모듈불러오기 

order_currency = 'BTC'   #변수 설정하기
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}' #링크를 문자열로 변환/ 정보 요청하기

response = requests.get(URL)  #응답받은 정보 변수설정

data = response.json()  #data는 클래스가 딕셔너리 /json으로 받기

print(data.get('data').get('prev_closing_price')) #data가 딕셔너리라서 .get 메서드사용/data에 있는 'data'에서 'prev_closing_price'받아오기
# data에 있는 전일종가를 추출하자