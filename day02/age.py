import requests

name = 'eric'
url = f'https://api.agify.io/?name={name}'

# response = requests.get(url)
# print(response)
# print(type(response))

response = requests.get(url).json()

# response 값 출력
print(response)

# response의 type 출력
print(type(response))

# 딕셔너리를 가져오므로 원하는 형식으로 출력해보자.
name = response['name']
age = response['age']

print(f'{name}님의 나이는 {age}세 입니다.')