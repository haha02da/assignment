users = {"Hans": "active", "Éléonore": "inactive", "Ken": "active"}
inactive_users = {}

for name, status in users.copy().items():
    if status == 'inactive':
        inactive_users[name] = status
        del users[name]


print("active users:", users)
print("inactive users:", inactive_users)
