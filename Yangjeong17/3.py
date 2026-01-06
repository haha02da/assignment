basket = ["apple","banana","apple","orange","banana","apple"]

unique_items = set(basket)
print("중복 제거:", unique_items)

counts = {}
for item in basket:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
print("품목별 개수:", counts)

sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("많이 담긴 순서:", sorted_items)

name_lengths = [len(item) for item in unique_items]
print("품목 이름 길이:", name_lengths)