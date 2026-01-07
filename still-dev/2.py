def is_balanced_brackets(s: str) -> bool:
    # 여기에 코드를 작성하면 됩니다.
    target = "{[()]}"
    del_char = "".join([char for char in s if char in "{[()]}"])

    
    
    for ch in s:
        if ch in check_list:



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