#과제 7

# 🧩 종합 미니 프로젝트(수업 마무리용)

## 프로젝트 A: 숫자 맞히기(up and down 게임 만들어보기)

# - 컴퓨터가 1~20 중 랜덤 숫자 선택
# - 사용자가 입력
# - if/elif로 “UP/DOWN/정답” 출력
# - 시도 횟수 5회 제한(range + for)
# - 성공하면 break, 실패하면 loop-else로 “실패” 출력

import random
target = random.randint(1,20)
#랜덤으로 숫자 뽑기
print(target)

for i in range(5):
    # 매 라운드마다 숫자를 입력 (특별히 마지막 라운드임을 강조)
    if i == 4:
        guess = int(input(f"마지막 {i+1}번째 시도입니다. 신중하게 숫자를 입력하세요."))
    else:
        guess = int(input(f"{i+1}번째 시도입니다. 숫자를 입력하세요:"))

    # 마지막 기회에는 UP/DOWN 말고 정답/실패만 나오게 설정
    if i == 4 and guess != target:
        continue
    
    # 예측과 목표숫자와의 비교 결과 프린트
    if guess > target:
        print("DOWN")
    elif guess < target:
        print("UP")
    elif guess == target:
        print("정답")
        break

#최종예측 실패시 for loop이 마무리되고 '실패'가 나옴
else:
    print("실패")

#솔루션
# import random

# answer = random.randint(1, 20)

# for chance in range(1, 6):  # 5번 기회
#     guess = int(input(f"{chance}번째 시도 (1~20): "))

#     if guess < answer:
#         print("UP")
#     elif guess > answer:
#         print("DOWN")
#     else:
#         print("정답입니다! 🎉")
#         break
# else:
#     print("실패! 정답은", answer)
