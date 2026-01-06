def is_balanced_brackets(s: str) -> bool:
  stack = []
  open = ['(', '{', '[']
  pair = {
    ')': '(',
    '}': '{',
    ']': '['
  }
  for char in s:
    if char in open:
      stack.append(char)
    elif char in pair:
      target = pair[char]
      if len(stack) == 0 or stack[-1] != target:
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