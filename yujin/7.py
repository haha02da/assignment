print("게임을 시작합니다(도전 횟수 총 5회).")
import random
num=list(range(1,21))
answer = random.choice(num)


for chance in range(1, 6):
    s = input("숫자 입력(20 이하):" ).strip()
    n = int(s)
    if n==answer:
        print("결과:", "정답입니다!")
        break

    elif n > answer:
        print("결과:", "down")
    elif n < answer:
        print("결과:", "up")
    else:
        print("실패입니다. 정답은", answer)
        break