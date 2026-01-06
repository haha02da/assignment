basket = ["apple","banana","apple","orange","banana","apple"]

unique_items = set(basket)
print("중복 제거:", unique_items)

counts = {}

for i in unique_items:
    counts[i] = basket.count(i)
print("품목별 개수:", counts)

sorted_items = sorted(counts.items())
print("많이 담긴 순서:", sorted_items)

name_lengths = []

for i in unique_items:
    name_lengths.append(len(i))

print("품목 이름 길이:", name_lengths)