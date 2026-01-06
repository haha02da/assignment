# 과제 1: 장바구니 품목 분석하기

# 1. 품목 리스트 입력(미리 제공해도 됨)
# 2. 중복 제거한 품목 출력(set)
# 3. 품목별 개수 출력(dict + count 또는 dict 누적)
# 4. 많이 담긴 순서대로 정렬해서 출력(sorted + key)
# 5. 품목 이름 길이 리스트 만들기(list comprehension)

basket = ["apple","banana","apple","orange","banana","apple"]


unique_items = set(basket)
print("중복 제거:", unique_items)
# set()- 중복 제거

counts = {}
for item in basket:
    counts[item] = counts.get(item, 0) + 1
print("품목별 개수:", counts)
# 품목별 갯수 세기: 딕셔너리 + get

sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("많이 담긴 순서:", sorted_items)


name_lengths = [len(item) for item in unique_items]
print("품목 이름 길이:", name_lengths)