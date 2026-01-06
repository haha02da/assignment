def is_balanced_brackets(s: str) -> bool:
    pair = {')':'(', ']':'[', '}':'{'}
    opens = set(pair.values())
    stack = []
    for i in s:
        if i in opens:
            stack.append(i)
        elif i in pair:
            if not stack or stack[-1] != pair[i]:
                return False
            stack.pop()

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