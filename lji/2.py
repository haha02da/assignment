def is_balanced_brackets(s: str) -> bool:
    stack = []
    opening = ['(','{','[']
    closing = [')','}',']']

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if opening.index(stack.pop()) != closing.index(char):
                return False
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