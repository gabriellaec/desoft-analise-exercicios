def login_disponivel(user,users):
    if not user in users:
        return user
    
    users_set = set(users)
    suffix = 1
    username = user + suffix 
    while username in users_set:
        suffix += 1
        username = username[:-1] + suffix
    return username