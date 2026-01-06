basket = ["apple","banana","apple","orange","banana","apple"]

unique_items = set(basket)
print("중복 제거:", unique_items)

counts = {}
for item in unique_items:
    counts[item] = basket.count(item)
print("품목별 개수:", counts)

sorted_items = sorted(counts)
print("많이 담긴 순서:", sorted_items)

name_lengths = [len(i) for i in basket]
# 여기에 코드를 작성하면 됩니다.
print("품목 이름 길이:", name_lengths)
