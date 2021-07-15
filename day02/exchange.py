# 현재 원/달러의 환율 구하기.

# requests 모듈 불러오기
import requests

# bs4 안에 있는 BeautifulSoup 기능을 사용
from bs4 import BeautifulSoup

# 시장지표를 확인하기위해 해당 url을 설정해준다.
url = 'https://finance.naver.com/marketindex/'

# url 에 보낸 요청의 text 값을 response 변수에 저장.
response = requests.get(url).text

# 하지만 보기에 좋지않다. -> 보기 좋게 만들기 위해 BeautifulSoup 사용.
# response 값을 bs 형태로 변경하면서 어떤 형태인지도 같이 적어준다음 data 변수에 저장.
data = BeautifulSoup(response, 'html.parser')

# >>> 인터넷 창에서 원하는 곳에 우클릭 - 검사 > 오른쪽 소스창에서 파란색으로 하이라이트 된 부분을 우클릭 - Copy - Copy selector
# 저장해둔 data에서 원하는 부분만을 뽑아오기위해 select_one을 사용하고
# 복사해온 값을 '' 안에 붙여넣은 다음 결과값을 won_dollar_exchange 에 저장.
won_dollar_exchange = data.select_one('#exchangeList > li.on > a.head.usd > div')

# 시장지표에서 원/달러 환율의 text 값만을 필요로 하므로 따로
result = won_dollar_exchange.text

# f-string 사용하여 원/달러 환율을 원하는 형식으로 출력.
print(f'현재 원/달러 환율은 {result} 입니다.')

# 환율만을 따로 표시해보자
value_won_dollar_exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
result_value = value_won_dollar_exchange.text
print(f'현재 원/달러 환율은 {result_value} 입니다.')

# 환율이 얼마인지, 최근 상승/하락 금액은 얼마인지도 나타내보자.
# 이건 굳이 copy 안해오더라도 span의 class 명을 보면 바꿀 수 있겠다.
change_won_dollar_exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.change')
blind_won_dollar_exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.blind')

# 똑같이 데이터의 text 값만을 저장해둔다.
result_change = change_won_dollar_exchange.text
result_blind = blind_won_dollar_exchange.text

# 원하는 모양으로 전체 결과값 f-string 사용하여 출력
print(f'현재 원/달러 환율은 1달러당 {result_value}원 입니다. 최근 {result_change}원 {result_blind} 하였습니다.')