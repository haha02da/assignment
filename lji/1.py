def is_balanced_parentheses(s: str) -> bool:
    # 여기에 코드를 작성하면 됩니다.

print(is_balanced_parentheses("(()())"))  # True
print(is_balanced_parentheses("(()"))     # False
print(is_balanced_parentheses("())"))     # False
print(is_balanced_parentheses("(hello(world))"))     # True
print(is_balanced_parentheses(")(abc("))     # False