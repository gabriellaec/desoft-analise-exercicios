def login_disponivel(login, lista):
    if not login in lista:
        return login
    else:
        i = 1
        while True:
            login2 = login+i
            if not login2 in lista:
                return login2
            i+=1
            