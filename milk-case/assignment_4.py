users = {"Hans": "active", "Éléonore": "inactive", "Ken": "active"}
inactive_users = []

for user in users.keys():
    if users[user] == 'inactive':
        inactive_users.append(user)

print("active users:", users)
print("inactive users:", inactive_users)