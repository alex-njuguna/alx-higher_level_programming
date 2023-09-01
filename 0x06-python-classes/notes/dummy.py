class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(User.id)