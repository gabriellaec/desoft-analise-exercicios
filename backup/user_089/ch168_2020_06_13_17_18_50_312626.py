def login_disponivel(login, lista):
    
    for e in lista:
        i = 1
        if login == e:
            login = login + str(i)
            lista.append(login)
        else:
            lista.append(login)
    return lista
