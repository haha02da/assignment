def is_balanced_brackets(s: str) -> bool:
    # 여기에 코드를 작성하면 됩니다.

    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    string = "{()}"
    for char in s:
        if char in bracket_map.values():  # 여는 괄호인 경우
            stack.append(char)
        elif char in bracket_map:  # 닫는 괄호인 경우
            if not stack or stack.pop() != bracket_map[char]:
                return False
    # 모든 순회가 끝난 후 스택이 비어있으면 균형이 맞는 것
    return len(stack) == 0

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