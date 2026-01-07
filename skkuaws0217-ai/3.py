basket = ["apple", "banana", "apple", "orange", "banana", "apple"]

# 1️⃣ 중복 제거한 품목 (set)
unique_items = set(basket)
print("중복 제거:", unique_items)

# 2️⃣ 품목별 개수 세기 (dict 누적)
counts = {}
for item in basket:
    counts[item] = counts.get(item, 0) + 1
print("품목별 개수:", counts)

# 3️⃣ 많이 담긴 순서대로 정렬 (value 기준 내림차순)
sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("많이 담긴 순서:", sorted_items)

# 4️⃣ 품목 이름 길이 리스트 (list comprehension)
name_lengths = [len(item) for item in basket]
print("품목 이름 길이:", name_lengths)
