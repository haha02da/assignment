import random

answer = random.randint(1, 20)

for i in range(5):
    choice = int(input("숫자를 입력하세요(1~20):"))

    if choice == answer:
        print("정답")
        break
    elif choice < answer:
        print("UP")
    else:
        print("Down")
else:
    print(f"'실패 정답은' {answer}")
