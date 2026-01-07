# # 🧩 종합 미니 프로젝트(수업 마무리용)

# ## 프로젝트: “장바구니 분석기”

# 요구사항:

# 1. 품목 리스트 입력(미리 제공해도 됨)
# 2. 중복 제거한 품목 출력(set)
# 3. 품목별 개수 출력(dict + count 또는 dict 누적)
# 4. 많이 담긴 순서대로 정렬해서 출력(sorted + key)
# 5. 품목 이름 길이 리스트 만들기(list comprehension)

basket = ["apple","banana","apple","orange","banana","apple"]

basket_set = set(basket)
basket_dict = {}
basket_sorted = []
basket_name_length_list = []

print("2. 중복을 제거한 품목 출력")
print(basket_set)

print("3. 품목별 갯수 출력")
for i in basket_set:
    basket_dict[i] = basket.count(i)
    #print(f"{i}의 갯수는 {basket.count(i)} 입니다.")
print(basket_dict)

print("4. 많이 담긴 순서대로 정렬된 리스트")
basket_sorted = sorted(basket_dict.items())
print(basket_sorted)

print("5. 품목 이름 길이 리스트")
basket_name_length_list = [len(fruit) for fruit in basket]
print(basket_name_length_list)