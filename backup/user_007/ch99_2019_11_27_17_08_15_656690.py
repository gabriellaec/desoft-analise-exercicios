def login_disponivel(login,lista):
    i = 1
    while login in lista:
        login += str(i)
        if login in lista:
            login = login[:len(login)-1]
        i += 1
    return login