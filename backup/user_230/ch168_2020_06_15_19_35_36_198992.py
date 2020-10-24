def login_disponivel(login, lista):
    novo_login=0
    num=0
    if login not in lista:
        lista.append(login)
    else:
        while login in lista:
            num+=1
            if login not in lista:
                lista.append(login+num)
                novo_login=login+num
    return novo_login