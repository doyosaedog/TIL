# Flask 불러온다
# Flask는 파이썬이 기본으로 가지고있는 모듈이 아니다.
# 설치를 위해 pip install Flask -> bash 창에 입력한다.
from flask import Flask, render_template, request
import requests

TOKEN = '1867821074:AAE9tMsP5yK5pQochAFWskaS0Q4WDLVBKfc'
url = f'https://api.telegram.org/bot{TOKEN}'
chat_id = 1812507892

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




# Flask로 어떤 문서를 응답할 때, return에 의해서 동작하는 것이 아니라
# 특정 문서 자체를 불러와서 응답할 수 있다.
# render_template
# flask가 가지고 있는 함수 render_template을 불러와야 한다.
# html 문서 하나 만들건데 그 문서를 보여주는 페이지 만들기


# ssafy page
@app.route("/ssafy")
def ssafy():
    return render_template('ssafy.html')


# write page
@app.route("/write")
def write():
    return render_template('write.html')


# send page
@app.route("/send")
def send():
    # print(request)
    # print(dir(request))
    
    # 날아온 message에서 message 받기
    message = request.args.get('message')
    # print(message)

    # 챗봇이 보낼 메세지와 대상
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={message}'

    # 메세지 보내기 요청
    requests.get(send_message_url)
    return render_template('send.html')

@app.route('/telegram', methods=['POST'])
def telegram():
    response = request.get_json()
    # print(response)
    chat_id = response['message']['from']['id']
    text = response['message']['text']

    if text == '누구야':
        text = f'{chat_id}님의 챗봇입니다.'
        
    elif text == '미세먼지':
        key = '%2BF%2BZ82MPkIbpFnSopUetyE3CrZHeF3vFIxBWr10XLe4aTo4inTS45tQXsxstitpAQJQS4V6yTcz4pdWS3STnfQ%3D%3D'
        sidoName = '부산'
        dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sidoName}&ver=1.0'
        response = request.get(dust_url).json()
        sido_name = response['response']['body']['items'][1]['sidoName']
        station_name = response['response']['body']['items'][1]['stationName']
        dust = response['response']['body']['items'][1]['pm10Value']
        text = f'{sido_name}{station_name}의 미세먼지 농도는{dust}입니다.'

    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_message_url)
    return '', 200

















if __name__ == '__main__':
    app.run(debug=True)