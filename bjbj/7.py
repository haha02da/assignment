import random


answer = random.randint(1,20)


for time in range(1,6):
    myanswer = int(input(f"기회는 총 5번입니다.\n{time}번째 기회 숫자를 넣어주세요",))
    
    if myanswer < answer :
        print("UP")
    
    elif myanswer > answer :
        print("down")

    else:
        print("정답입니다. 축하합니다!")
        break
else:
    print(f"기회를 모두 소진하셨습니다. 정답은{answer}입니다.")