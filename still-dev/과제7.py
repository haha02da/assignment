# # 과제7

# # 🧩 종합 미니 프로젝트(수업 마무리용)

# ## 프로젝트 A: 숫자 맞히기(up and down 게임 만들어보기)

# - 컴퓨터가 1~20 중 랜덤 숫자 선택
# - 사용자가 입력
# - if/elif로 “UP/DOWN/정답” 출력
# - 시도 횟수 5회 제한(range + for)
# - 성공하면 break, 실패하면 loop-else로 “실패” 출력

# ```python
import random

selected_number = random.randint(1,20)
user_num = 0
try_num = 5

while try_num:
    user_num = input("숫자를 입력해주세요. \n")

    if user_num.isdigit():
        user_num = int(user_num)
        if 1 <= user_num <= 20:
            if user_num == selected_number:
                print("정답입니다.")
                break
            elif user_num > selected_number:
                print("DOWN")
                try_num -= 1
                print(f"남은 시도횟수 : {try_num}회")
            else:
                print("UP")
                try_num -= 1
                print(f"남은 시도횟수 : {try_num}회")
        else:
            print("잘못된 입력입니다. 1~20 사이 정수를 입력해주세요.")    
    else:
        print("문자는 입력불가. 1~20 사이 정수를 입력해주세요.")
        
if try_num == 0:
    print(f"실패!!! 정답은 {selected_number} 입니다")      
    

