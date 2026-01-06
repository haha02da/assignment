users = {"Hans": "active", "Éléonore": "inactive", "Ken": "active"}

# for user, status in users.copy().items():
#     if status == "inactive":
#         del users[user]

# print(users)

for user, status in users:
    if status == "inactive":
        print(user, status)