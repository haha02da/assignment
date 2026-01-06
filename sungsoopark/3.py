# 과제 3

# 🧩 종합 미니 프로젝트(수업 마무리용)

## 프로젝트: “장바구니 분석기”

# 요구사항:

# 1. 품목 리스트 입력(미리 제공해도 됨)
# 2. 중복 제거한 품목 출력(set)
# 3. 품목별 개수 출력(dict + count 또는 dict 누적)
# 4. 많이 담긴 순서대로 정렬해서 출력(sorted + key)
# 5. 품목 이름 길이 리스트 만들기(list comprehension)
# 1.
basket = ["apple","banana","apple","orange","banana","apple"]
# 2.
basket_set = set(basket)
print(basket_set)
# 3.
# 3-1
basket_dict_1 = {}

for i in basket:
    if i in basket_dict_1.keys():
        basket_dict_1[i] += 1
    else:
        basket_dict_1[i] = 1
# 3-2
basket_dict_2 = {}
for i in basket_set:
    basket_dict_2[i] = basket.count(i)

print(basket_dict_1)
print(basket_dict_2)

# 4.
sorted_basket_dict = sorted(basket_dict_1.items(), key=lambda x: x[1], reverse=True)
print(sorted_basket_dict)

# 5.
basket_list = []
for i,p in basket_dict_1.items():
    basket_list.append("{}의 글자수는 {}입니다".format(i,len(i)))
print("중복 제거:", basket_set)
print("품목별 개수:", basket_dict_2)
print("많이 담긴 순서:", sorted_basket_dict)
print("품목 이름 길이:", basket_list)

#솔루션
# basket = ["apple", "banana", "apple", "orange", "banana", "apple"]

# # 1️⃣ 중복 제거한 품목 (set)
# unique_items = set(basket)
# print("중복 제거:", unique_items)

# # 2️⃣ 품목별 개수 세기 (dict 누적)
# counts = {}
# for item in basket:
#     counts[item] = counts.get(item, 0) + 1
# print("품목별 개수:", counts)

# # 3️⃣ 많이 담긴 순서대로 정렬 (value 기준 내림차순)
# sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
# print("많이 담긴 순서:", sorted_items)

# # 4️⃣ 품목 이름 길이 리스트 (list comprehension)
# name_lengths = [len(item) for item in basket]
# print("품목 이름 길이:", name_lengths)

# print("중복 제거:", unique_items)
# print("품목별 개수:", counts)
# print("많이 담긴 순서:", sorted_items)
# print("품목 이름 길이:", name_lengths)