def is_balanced_parentheses(s: str) -> bool:
    storage = []
    for char in s:
        if char == '(':
            storage.append(char)
        elif char ==')':
            if len(storage) <= 0:
                return False
            storage.pop()
        else:
            continue
    if len(storage) > 0:
        return False
    else:
        return True

print(is_balanced_parentheses("(()())"))  # True
print(is_balanced_parentheses("(()"))     # False
print(is_balanced_parentheses("())"))     # False
print(is_balanced_parentheses("(hello(world))"))     # True
print(is_balanced_parentheses(")(abc("))     # False