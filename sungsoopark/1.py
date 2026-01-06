## 과제1

#괄호 검사(간단): `"(()())"` 문자열을 읽으며 push/pop으로 균형 확인(확장 과제)

def is_balanced_parentheses(code):
    code = list(code)
    front_tuple = code.count("(")
    back_tuple = code.count(")")
    if front_tuple != 0 and front_tuple == back_tuple:
        for i in range(1,back_tuple):
            first_back_tuple = code.index(")")
            code.remove(")")
            if code[:first_back_tuple].count("(") != 0:
                index_of_matched_front_tuple = len(code) - 1 - code[:first_back_tuple].index('(')
                code.pop(index_of_matched_front_tuple)
        return True
    else:
        return False   


is_balanced_parentheses("(()())") # True
print(is_balanced_parentheses("(()())"))  # True
print(is_balanced_parentheses("(()"))     # False
print(is_balanced_parentheses("())"))     # False
print(is_balanced_parentheses("(hello(world))"))     # True
print(is_balanced_parentheses(")(abc("))     # False
print(is_balanced_parentheses("Hello World")) # False


#솔루션
# def is_balanced_parentheses(s: str) -> bool:
#     stack = []
#     for ch in s:
#         if ch == '(':
#             stack.append(ch)      # push
#         elif ch == ')':
#             if not stack:         # pop할 게 없음
#                 return False
#             stack.pop()           # pop
#     return len(stack) == 0        # 남아있으면 '('가 남은 것

# print(is_balanced_parentheses("(()())"))  # True
# print(is_balanced_parentheses("(()"))     # False
# print(is_balanced_parentheses("())"))     # False
# print(is_balanced_parentheses("(hello(world))"))     # True
# print(is_balanced_parentheses(")(abc("))     # False