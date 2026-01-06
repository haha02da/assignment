prime_numbers = []

for i in range(2, 51):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1

    if count == 0:
        prime_numbers.append(i)

print("prime numbers(2~50)\n", prime_numbers)