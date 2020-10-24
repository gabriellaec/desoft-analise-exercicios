def login_disponivel(login, lista):
    i = 1
    if login not in lista:
        return login
    else:
        while login in lista:
            login = login+str(i)
            if login in lista:
                login = login[:-1]                    
            i+=1
    return login