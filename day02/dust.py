import requests

key = '%2BF%2BZ82MPkIbpFnSopUetyE3CrZHeF3vFIxBWr10XLe4aTo4inTS45tQXsxstitpAQJQS4V6yTcz4pdWS3STnfQ%3D%3D'
sidoName = input('시/도 이름을 입력하세요.\n 전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종 \n')
input_station_name = input('동 이름을 입력하세요. \n')
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sidoName}&ver=1.0'

response = requests.get(url).json()

# print(response)

items = response['response']['body']['items']

for value in items:
    if value['stationName'] == input_station_name:
        station_name = value['stationName']
        pm10Value = value['pm10Value']


# 내 고향의 이름이 잘 나오는지 확인하기.
# station_name = response['response']['body']['items'][39]['stationName']

# print(station_name)

# pm10Value 받아오기.
# pm10Value = response['response']['body']['items'][39]['pm10Value']

# print(pm10Value)
# print(type(pm10Value))

# if문 활용하여 미세먼지 좋음 ~ 매우나쁨 보기
condition_now = ''

if int(pm10Value) > 150:
    condition_now = '매우 나쁨!'
elif int(pm10Value) > 80:
    condition_now = '나쁨..'
elif int(pm10Value) > 30:
    condition_now = '보통'
else:
    condition_now = '좋음!'
# 정리 및 f-string

print(f'지금 {station_name}의 미세먼지 농도는 {pm10Value}, {condition_now} 입니다.')