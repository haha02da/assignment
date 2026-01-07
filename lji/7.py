import random

answer = random.randint(1, 20)

chance = 5
while chance > 0:
    trial = int(input("Enter your guess (1~20): "))
    if trial < 1 or trial > 20:
        print("Enter again; Out of range.")
    elif trial < answer:
        print("UP")
        chance -= 1
    elif trial > answer:
        print("DOWN")
        chance -= 1
    else:
        print("Correct!")
        break

else:
    print(f"Failed. The answer is {answer}.")