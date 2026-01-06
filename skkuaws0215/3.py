## 프로젝트: “장바구니 분석기”
# 요구사항:
# 1. 품목 리스트 입력(미리 제공해도 됨)
# 2. 중복 제거한 품목 출력(set)
# 3. 품목별 개수 출력(dict + count 또는 dict 누적)
# 4. 많이 담긴 순서대로 정렬해서 출력(sorted + key)
# 5. 품목 이름 길이 리스트 만들기(list comprehension)


basket = ["apple","banana","apple","orange","banana","apple"]

# 여기에 코드를 작성하면 됩니다.
unique_items = set(basket)
print(unique_items)
print("중복 제거:", unique_items)

# 여기에 코드를 작성하면 됩니다.
counts = {}
for items in basket:
    counts[items] = counts.get(items, 0) + 1
print("품목별 개수:", counts)

# 여기에 코드를 작성하면 됩니다.
sorted_items = sorted(counts.items(), key = lambda x: x[1], reverse = True)
print("많이 담긴 순서:", sorted_items)

# 여기에 코드를 작성하면 됩니다.
name_lengths = set(basket)
name_lengths = [(items) for items in unique_items]
print("품목 이름 길이:", name_lengths)
print()