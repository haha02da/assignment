basket = ["apple","banana","apple","orange","banana","apple"]

# 여기에 코드를 작성하면 됩니다.
unique_items = set(basket)
print("중복 제거:", unique_items)

# 여기에 코드를 작성하면 됩니다.
counts = {i: basket.count(i) for i in unique_items}
print("품목별 개수:", counts)

# 여기에 코드를 작성하면 됩니다.
sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("많이 담긴 순서:", sorted_items)

# 여기에 코드를 작성하면 됩니다.
name_lengths = {item: len(item) for item in unique_items}
print("품목 이름 길이:", name_lengths)

print("과제 3 제출")