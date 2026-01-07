#프로젝트 A: 숫자 맞히기(up ad down 게임 만들기)

# - 컴퓨터가 1~20 중 랜덤 숫자 선택
# - 사용자가 입력
# - if/elif로 “UP/DOWN/정답” 출력
# - 시도 횟수 5회 제한(range + for)
# - 성공하면 break, 실패하면 loop-else로 “실패” 출력 

import random

def get_start():
    #1~20까지 랜덤 숫자 선택
    target = random.randint(1,20)
    print("1~20 중, 숫자를 입력해보세요! 기회는 단, 5번!")
    

    for i in range(1,6):
        user_guess_number = int(input(f"[{i}회차] 숫자를 입력하세요: "))

        if user_guess_number < target:
            print ("Up")
        elif user_guess_number > target:
            print ("Down")
        else: 
            print ("정답")
            break
    
    else:
        print ("실패")

get_start()
