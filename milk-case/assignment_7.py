import random
import time
import sys

class OutOfRangeError(Exception):
    def __init__(self):
        super().__init__('Enter only numbers between 1 to 20!')

def up_down_game():
    answer = random.randint(1,20)
    print("Random Number Generated!")
    print("------ GAME START ------")

    for cnt in range(1,6):
        print(f"Enter Your Answer(1~20) --- #({cnt} / 5)")
        while True:
            try:
                user_input = int(sys.stdin.readline())
                if user_input < 1 or user_input > 20:
                    raise OutOfRangeError
                break
            except OutOfRangeError as e:
                print(e)
            except ValueError:
                print('Enter only numbers between 1 to 20!')

        if user_input > answer:
            print('DOWN')
        elif user_input < answer:
            print('UP')
        else:
            print('정답\n')
            break

    print('실패\n')
    return
    
while True:
    up_down_game()
    time.sleep(2)
