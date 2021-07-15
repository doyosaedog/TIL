# greeting 이라는 변수에 '안녕하세요' 라는 문자를 할당한다.
greeting = '안녕하세요.'

# 주석처리 하는법 : ctrl + /
# greeting 변수가 담고있는 값을 출력한다.
# print(greeting)

# 반복문을 통해서 인사를 여러번 해보도록 하자.

# while

count=0
while count<4:
    print(greeting)
    count += 1

# for

# 0~ n-1 까지의 숫자들을 만들어주는 range()
# range(5) -> 0,1,2,3,4

# i -> 0~4까지의 값을 반복해서 넣는다.
for i in range(5):
    print(i,greeting)