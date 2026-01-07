import random

number = list(range(1,21))

pick = random.choice(number)

for chance in range(1,6):
    an = int(input("Guess! "))

    if an < 1 or an > 20:
        print("pick a number from 1 to 20")
    elif an < pick:
        print("Up")
    elif an > pick:
        print("Down")
    else:
        print("Congrats!")
        break
else:
    print("Not a chance;P Answer is :", pick)
