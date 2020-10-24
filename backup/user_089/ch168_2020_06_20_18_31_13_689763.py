def login_disponivel(login, lista):
    i = 1
    if login not in lista:
        lista.append(login)
    else:
        for e in lista:
            if login == e:
                login = login + str(i)
                lista.append(login)
                i += 1
    
    return lista