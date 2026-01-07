
import random
lotto = random.randint(1, 20)  # 여러 개 뽑을 땐 range를 쓰고 지금 문제에선 1~20 중 숫자 1개 뽑는거니까 radient를 씀.. # radint(1,20)은 1이상 20이하
for i in range(5):   # 총 5번 시도
    guess = int(input("숫자를 입력하세요 (1~20): "))

    if guess < lotto:
        print("UP")
    elif guess > lotto:
        print("DOWN")
    else:
        print("정답입니다!")
        break
else:
    print("실패! 정답은", lotto)

 
