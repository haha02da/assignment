basket = ["apple","banana","apple","orange","banana","apple"]
# 중복 제거한 품목 출력 (set)
unique_items = set(basket)
print("중복 제거:",unique_items)

# 품목별 개수 출력 (dict 누적)
counts = {}

for item in basket:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] =1

print("품목별 개수:", counts)

# 많이 담긴 순서대로 정렬 ( sorted + key )
sorterd_items = sorted(counts.items(), key=lambda x: x[1],reverse=True)
print("많이 담긴 순서:", sorterd_items)

#품목 이름 길이 리스트 만들기
name_lengths = [len(item) for item in unique_items]
print("품목 이름 길이", name_lengths)

