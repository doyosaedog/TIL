# 숫자 타입
number = 3
print(type(number))

# 문자열
string = '문자열'
print(type(string))

# boolean
boolean = True
print(type(boolean))

# 형변환
string_number = '58'

# 문자열과 숫자는 연산이 안된다.
# print(string_number + 5)

# 정수형으로 변환하자.
print(type(int(string_number)))

# f-string / string interpolation / f 문자열
name = '홍길동'
print(f'{name}입니다. 반갑습니다.')

"""
주석입니다.
얘는 여러 줄이 가능해요.
편하죠?

리스트
"""

# list 선언
my_list = ['java','python']
print(my_list)

# list 원소 접근 : List[index]
print(my_list[0])

# list 원소 변경
my_list[0] = 'django'
print(my_list[0])

# list 길이 : len() 함수. length
print(len(my_list))


"""
딕셔너리
"""

# 딕셔너리 선언
my_info = {
    'name': '조영현',
    'age': 27 
}
print(my_info)

# 딕셔너리 원소 접근방법 2가지

# 1
print(my_info['name'])

# 가지고있지않은 key로 접근을 시도하면
# print(my_info['location'])
# 오류가 나온다.

# 2
print(my_info.get('name'))

# get 방식을 사용하면 get 함수를 


# 딕셔너리 원소 변경