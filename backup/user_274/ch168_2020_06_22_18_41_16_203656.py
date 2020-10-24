def login_disponivel(login, lista):
    c = 0
    if login not in lista:
        return login
    else:
        for i in lista:
            if i[:len(login)] == login:
                 c = c+1  
        return login+str(c)
        