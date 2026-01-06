# 과제4
# inactive 사용자만 따로 inactive_users dict로 모아보기(새 컬렉션 전략) 구현해줘.

users = {"Hans": "active", "Éléonore": "inactive", "Ken": "active"}
inactive_users = {}
for user, status in users.copy().items():
    if status == "inactive":
        inactive_users[user]=status
        del users[user]
# 여기에 코드를 작성하면 됩니다.

print("active users:", users)
print("inactive users:", inactive_users)