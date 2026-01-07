import random

# 여기에 코드를 작성하면 됩니다.
random_count = random.randint(1, 20)

for answer in range(5) :
    answer = int(input("정답은?(1~20 중 정수) :"))
    if answer > random_count :
        print("다운")
    elif answer < random_count :
        print("업")
    else :
        print("정답!")
        break

else :
    print(f"정답을 맞추지 못하였습니다. 정답은 {random_count}입니다.")