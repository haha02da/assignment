# ✅ 품목 리스트
basket = ["apple","banana","apple","orange","banana","apple"]

# 🛒 중복 제거한 품목 출력
unique_items = set(basket)
print("중복 제거:", unique_items)

# 🛒 품목별 개수 출력
counts = {}
for i in unique_items:
  counts[i] = basket.count(i)
print("품목별 개수:", counts)

# 🛒 많이 담긴 순서대로 정렬해서 출력
sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("많이 담긴 순서:", sorted_items)

# 🛒 품목 이름 길이 리스트 만들기
name_lengths = [len(item) for item in basket]
print("품목 이름 길이:", name_lengths)