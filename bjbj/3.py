basket = ["apple","banana","apple","orange","banana","apple"]
unique_items = set(basket)
# 여기에 코드를 작성하면 됩니다.
print("중복 제거:", unique_items)

counts = {}

for fruite in basket:
    if fruite in counts :
        counts[fruite]  += 1
    else:
        counts[fruite]= 1


# 여기에 코드를 작성하면 됩니다.
print("품목별 개수:", counts)

sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
# 여기에 코드를 작성하면 됩니다.
print("많이 담긴 순서:", sorted_items)

name_lengths = [len(fruite) for fruite in unique_items] 
# 여기에 코드를 작성하면 됩니다.
print("품목 이름 길이:", name_lengths)