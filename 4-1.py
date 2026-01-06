4n = int(input("2 이상의 정수: "))

for x in range(2, n):
    if n % x == 0:
        print("합성수! 약수:", x)
        break
