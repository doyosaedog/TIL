# requests 불러오기
import requests

from pprint import pprint

# 장난용
# PF_TOKEN = '1855765985:AAF11tyL1neSuqWqGEnUIlNHSCna3GFGRTs'
# PF_KEY = '1582657480'
# url_pf = f'https://api.telegram.org/bot{PF_TOKEN}'
# text_to_pf = '점심 맛있게 드세요!'

# 봇 토큰 변수에 담기
TOKEN = '1867821074:AAE9tMsP5yK5pQochAFWskaS0Q4WDLVBKfc'

# url 설정
url = f'https://api.telegram.org/bot{TOKEN}'


# 테스트
# print(url)

# 내 챗봇에 메세지 보낸사람 ID 확인하기
get_updates_url = f'{url}/getUpdates'

# 테스트
# print(get_updates_url)

# 챗봇이 받은 메세지 json 형식으로 받아서 response에 저장
response = requests.get(get_updates_url).json()

# 테스트
# pprint(response)

# 챗봇이 받은 메세지와 보낸사람의 ID만 추출하기
chat_id = response['result'][0]['message']['from']['id']
text = response['result'][0]['message']['text']

print(chat_id,text)

# 메세지 보낸 사람에게 답장하는 url 만들기
send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'

# 교수님한테 장난쳐보기
# send_message_url_pf = f'{url_pf}/sendMessage?chat_id={PF_KEY}&text={text_to_pf}'

# 답장기능 작동
requests.get(send_message_url)

# 드가보자~
# requests.get(send_message_url_pf)