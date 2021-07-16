import requests

PF_TOKEN = '1855765985:AAF11tyL1neSuqWqGEnUIlNHSCna3GFGRTs'
PF_KEY = '1582657480'
url_pf = f'https://api.telegram.org/bot{PF_TOKEN}'
text_to_pf = '점심 맛있게 드세요!'

send_message_url_pf = f'{url_pf}/sendMessage?chat_id={PF_KEY}&text={text_to_pf}'

requests.get(send_message_url_pf)