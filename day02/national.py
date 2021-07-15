import requests

name = 'jo'
url = f'https://api.nationalize.io/?name={name}'

# response = requests.get(url)
# print(response)
# print(type(response))

response = requests.get(url).json()

# response 값 출력
print(response)

# response의 type 출력
# print(type(response))

# 딕셔너리를 가져오므로 원하는 형식으로 출력해보자.
country = response['country'][0]['country_id']
probability = response['country'][0]['probability'] * 100
print(country)
print(probability)

# 자 이제 형식을 갖춰보자
print(f'{name}님의 국가는 {country}이며, 확률은 {round(probability,2)} % 입니다.')