#과제 5

#2~50 사이의 소수 목록 출력하기(과제)
for i in range(2,51):
    for x in range(2,i):
        if i % x == 0:
            break
    else:
        print(i)


#솔루션
# for n in range(2, 51):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else:
#         print(n, end=" ")
