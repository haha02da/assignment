#과제 2

#여러 종류 괄호 ()[]{}까지 검사
def is_balanced_brackets(s: str) -> bool:
    # 여기에 코드를 작성하면 됩니다.
    s = list(s)
    frontbracketlist = ['{',  '[',  '(']
    backbracketlist = ['}', ']', ')']

    stack = []
    for i in s:
        if i in frontbracketlist:
            stack.append(i)
        elif i in backbracketlist:
            if i == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    if stack == []:
        return True
    else:
        return False

print(is_balanced_brackets("{[()()]}"))  # True
print(is_balanced_brackets("{[(])}"))    # False
print(is_balanced_brackets("([)]"))      # False
print(is_balanced_brackets('''{       
  "id": "user-001",
  "name": "Jinyoung Choi",
  "active": true,
  "createdAt": "2026-01-03T10:30:00Z",
  "projects": [
    {
      "projectId": "p-100",
      "title": "Cloud Migration",
      "status": "in-progress"
    },
    {
      "projectId": "p-200",
      "title": "DevOps Automation",
      "status": "completed"
    }
  ]
}
'''))                                     # True


#솔루션
# def is_balanced_brackets(s: str) -> bool:
#     pair = {')': '(', ']': '[', '}': '{'}
#     opens = set(pair.values())
#     stack = []

#     for ch in s:
#         if ch in opens:
#             stack.append(ch)
#         elif ch in pair:  # 닫는 괄호
#             if not stack or stack[-1] != pair[ch]:
#                 return False
#             stack.pop()

#     return len(stack) == 0

# print(is_balanced_brackets("{[()()]}"))  # True
# print(is_balanced_brackets("{[(])}"))    # False
# print(is_balanced_brackets("([)]"))      # False
# print(is_balanced_brackets('''{       
#   "id": "user-001",
#   "name": "Jinyoung Choi",
#   "active": true,
#   "createdAt": "2026-01-03T10:30:00Z",
#   "projects": [
#     {
#       "projectId": "p-100",
#       "title": "Cloud Migration",
#       "status": "in-progress"
#     },
#     {
#       "projectId": "p-200",
#       "title": "DevOps Automation",
#       "status": "completed"
#     }
#   ]
# }
# '''))                                     # True
