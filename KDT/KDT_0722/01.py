# - 인기 영화 목록의 개수를 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# - 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.


import requests    # 모듈을 불러온다.
import os
from dotenv import load_dotenv

load_dotenv()
MV_API_KEY = os. environ.get("MV_API_KEY")


def popular_count():

    #URL로 요청보내서 원하는 정보 받기.
    MV_URL = 'https://api.themoviedb.org/3'   #베이스URL로 여기는 계속 같은 값
    path = '/movie/popular'                   # 원하는 정보 요청 /어떤 것을 원하느냐에 따라 변경(원하는 홈페이지에서 제공)

    params = {
        'api_key': MV_API_KEY,  #내 APi key 입력
        'language': 'ko-KR'     #언어변경                
 }

    response = requests.get(MV_URL+path, params=params).json() #응답받은 정보 변수 정하기. requests라는 딕셔너리에서 키값과 벨류값을 json으로 받겠다.
    #응답 받은 값을 가져온다.
    return len(response["results"]) #함수리턴하기(함수는 리턴이 있어야 값추출할 수 있음)/ response에 있는 "results"를 list로 변환하고 길이로 반환하기. / results가 몇개인지 구하는 방법.

    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20