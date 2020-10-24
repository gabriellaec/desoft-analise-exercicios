def login_disponivel(user,users):
    if not user in users:
        return user
    
    users_set = set(users)
    suffix = 1
    username = user + str(suffix)
    while username in users_set:
        suffix += 1
        username = username[:-1] + str(suffix)
    return username
names = []
name = input()
while name != "fim":
    names.append(login_disponivel(name,names))
    name = input()
for name in names:
    print(name)
     