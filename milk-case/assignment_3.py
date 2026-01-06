import sys

print("<< INSERT ITEM LIST >>")
basket = list(map(str, sys.stdin.readline().split()))

basket_set = set(basket)
print('\n> Without duplication')
print(*basket_set, "\n")

basket_dict = {fruit : basket.count(fruit) for fruit in basket_set}
print('> Quantity per item')
print(basket_dict, "\n")

basket_sorted = sorted(basket_dict.items(), key=lambda x: x[1], reverse=True)
print('> Sorted by quantity')
print(*basket_sorted, '\n')

basket_len = {fruit : len(fruit) for fruit in basket_set}
print('> Length of items')
print(basket_len)