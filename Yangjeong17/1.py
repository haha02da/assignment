def is_balanced_parentheses(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced_parentheses("(()())"))  # True
print(is_balanced_parentheses("(()"))     # False
print(is_balanced_parentheses("())"))     # False
print(is_balanced_parentheses("(hello(world))"))     # True
print(is_balanced_parentheses(")(abc("))     # False