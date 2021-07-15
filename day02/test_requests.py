# 파이썬으로 요청보내기 위한 준비
# requests 모듈을 사용하기위해 불러오기
import requests

# requests로 https://www.naver.com 으로 요청 보내본 결과 받아보기.
print(requests.get('https://www.naver.com'))

# requests로 https://www.naver.com 으로 요청 보내본 결과의 텍스트를 받아보기.
# print(requests.get('https://www.naver.com').text)

# requests로 https://www.naver.com 으로 요청 보내본 결과의 status_code를 받아보기.
print(requests.get('https://www.naver.com').status_code)
