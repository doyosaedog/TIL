# 무작위로 뽑기위해서 random을 쓸건데,
# 이 random은 그냥 쓸 수는 없고 어딘가에서 가져와야 한다.
# 불러오는 방법은 import를 사용한다.
import random

# lunch라고 하는 변수에 점심메뉴 3가지를 넣어보자.
# 점심메뉴 추천 받습니다.

# 리스트를 만들때 중요한 것은 대괄호
# 그 안에 담긴 요소들 -> 문자열이라면 전부 따옴표 ''
# 쉼표로 구분 해준다.

lunch = ['짜장','돈가스','냉면']

# lunch 전체 출력
print(lunch)

# lunch 3번째 요소(볶음밥) 출력
print(lunch[2])

# lunch가 가지고있는 메뉴중에 하나를 무작위로 골라서
# menu라는 변수에 담는다.
menu = random.choice(lunch)
print(menu)