basket = ["apple","banana","apple","orange","banana","apple"]

unique_items = set(basket)
print("중복 제거:", unique_items)

counts = {}
for item in basket:
    counts[item] = basket.count(item)
print("품목별 개수:", counts)

sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("많이 담긴 순서:", sorted_items)

name_lengths = [len(item) for item in basket]
print("품목 이름 길이:", name_lengths)