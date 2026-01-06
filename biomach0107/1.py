def is_balanced_parentheses(s: str) -> bool:
    
    stack = []
    for char in s:
        if char == '(':  # 여는 괄호인 경우
            stack.append(char)
        elif char == ')':  # 닫는 괄호인 경우
            if not stack:  # 스택이 비어있으면 균형이 맞지 않음
                return False
            stack.pop()  # 여는 괄호와 짝이 맞으므로 스택에서 제거
    # 모든 순회가 끝난 후 스택이 비어있으면 균형이 맞는 것
    return len(stack) == 0

print(is_balanced_parentheses("(()())"))  # True
print(is_balanced_parentheses("(()"))     # False
print(is_balanced_parentheses("())"))     # False
print(is_balanced_parentheses("(hello(world))"))     # True
print(is_balanced_parentheses(")(abc("))     # False