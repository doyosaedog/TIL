# requests 모듈 불러오기
import requests

# bs4 안에 있는 BeautifulSoup 기능을 사용
from bs4 import BeautifulSoup

# KOSPI를 확인하기위해 해당 url을 설정해준다.
url = 'https://finance.naver.com/sise/'

# url 에 보낸 요청의 text 값을 response 변수에 저장.
response = requests.get(url).text

# 값을 출력
# print(response)
# 하지만 보기에 좋지않다. -> 보기 좋게 만들기 위해 BeautifulSoup 사용.

# response 값을 bs 형태로 변경하면서 어떤 형태인지도 같이 적어준다음 data 변수에 저장.
data = BeautifulSoup(response, 'html.parser')

# data의 type을 출력해보자.
# print(type(data))

# >>> 인터넷 창에서 원하는 곳에 우클릭 - 검사 > 오른쪽 소스창에서 파란색으로 하이라이트 된 부분을 우클릭 - Copy - Copy selector
# 저장해둔 data에서 원하는 부분만을 뽑아오기위해 select_one을 사용하고
# 복사해온 값을 '' 안에 붙여넣은 다음 결과값을 KOSPI에 저장.
KOSPI = data.select_one('#KOSPI_now')

# KOSPI를 출력
# print(KOSPI)

# KOSPI의 type 출력
# print(type(KOSPI))

# KOSPI 의 text 값만을 필요로 하므로 따로
result = KOSPI.text

# f-string 사용하여 KOSPI 수치를 원하는 형식으로 출력.
print(f'현재 KOSPI 지수는 {result} 입니다.')

# f-string 없이 출력도 가능.
print('현재 KOSPI 지수는', result, '입니다.')