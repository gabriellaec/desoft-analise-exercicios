def login_disponivel(user, lista):
    i = 1
    login = user
    for k in lista:
        if login == k:
            login = user + str(i)
            i += 1
    return login
 
        