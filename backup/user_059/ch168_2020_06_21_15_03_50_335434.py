def login_disponivel(login, lista):
    if login not in lista:
        return login
    else:
        cont = 0
        for i in lista:
            if login in i:
                cont +=1
        return login+str(cont)