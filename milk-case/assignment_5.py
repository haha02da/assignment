import sys

n = int(sys.stdin.readline())

if n < 2:
    print(0)

else:
    arr = [i for i in range(n+1)]

    for i in range(2, int(n ** (1/2) + 1)):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
    res = [i for i in arr[2:] if arr[i]]
    
    print(f"<< {n} 이하의 소수 리스트 >>")
    print(*res)