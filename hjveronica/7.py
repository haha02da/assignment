import random

auto_num=random.randrange(1,21)

for n in range(1,6):
    user_num=int(input(f"input number (1~20): "))

    if user_num < auto_num:
        print("UP")
    elif user_num > auto_num:
        print("Down")
    else:
        print("정답")
        break

else: 
    print("실패")
