import random
#if/elif로 up/down/정답 결정, 시도횟수 5회 제한(range + for문 활용)
#성공하면 break, 실패하면 loop-else로 "실패" 출력 size 

answer: int = random.randint(1, 20)

for attempt in range(5):
    guess = int(input("1부터 20 사이의 숫자를 맞춰보세요: "))

    if guess < answer:
        print("Up!")
    elif guess > answer:
        print("Down!")
    else:
        print("정답입니다!")
        break
else:
    print(f"실패! 정답은 {answer}였습니다.") 
