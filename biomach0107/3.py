basket = ["apple","banana","apple","orange","banana","apple"]

# 여기에 코드를 작성하면 됩니다.


# 중복 제거한 품목 (set)
unique_items = set (basket)
print(f"1. 중복 제거 품목: {unique_items}")

#품목별 개수 세기 (dictionary)
item_counts = {}
for item in basket:
    item_counts[item] = item_counts.get(item,0) + 1
print(f"2. 품목별 개수: {item_counts}")

# 많이 담긴 순서대로 정렬(value 기준 내림차순)
#item_counts.items()는 (품목, 개수) 형태의 튜플 리스트를 반환합니다
sorted_items = sorted(item_counts.items(), key=lambda x: x[1], reverse=True)
print("3. 많이 담긴 순서 정렬:")
for item, count in sorted_items:
    print(f"   - {item}: {count}개")

# 품목 이름 길이 리스트 (list comprehension)
name_lengths = [len(item) for item in unique_items]
print(f"4.품목 이름 길이 리스트: {name_lengths}")

# 총 개수 (sum)
total_count = sum(item_counts.values())
print(f"5.총 개수: {total_count}개")    