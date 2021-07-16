# setWebHook 요청 보내야하니까
import requests

# TOKEN, url, ngrok url 필요
TOKEN = '1867821074:AAE9tMsP5yK5pQochAFWskaS0Q4WDLVBKfc'
url = f'https://api.telegram.org/bot{TOKEN}'
# ngrok_url = 'https://f287d76ca215.ngrok.io'
python_anywhere = 'https://loveyh95.pythonanywhere.com'
set_webhook_url = f'{url}/setWebhook?url={python_anywhere}/telegram'

# telegram이 내 ngrok/telegram 으로 요청을 보내고 200 응답 받아간다.
response = requests.get(set_webhook_url)
print(response.text)