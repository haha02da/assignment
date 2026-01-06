basket = ["apple","banana","apple","orange","banana","apple"]

# # 여기에 코드를 작성하면 됩니다.
unique_items = set(basket)
print("중복 제거:", unique_items)

# # # 여기에 코드를 작성하면 됩니다.
counts = {}

for fruits in basket :
    if fruits in counts :
        counts[fruits] = counts[fruits] + 1
    else :
        counts[fruits] = 1
print("품목별 개수:", counts)

# # 여기에 코드를 작성하면 됩니다.
def get_count(item) :
    return item[1]

sorted_items = sorted(counts.items(), key = get_count, reverse = True)
print("많이 담긴 순서:", sorted_items)

# # 여기에 코드를 작성하면 됩니다.
name_lengths = [len(item) for item in basket]
print("품목 이름 길이:", name_lengths)