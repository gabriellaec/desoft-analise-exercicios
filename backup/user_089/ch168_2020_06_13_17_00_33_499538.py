def login_disponivel(login, lista):
    i = 1
    for e in lista:
        if login == e:
            lista.append(login + (i))
            i += 1
        else: 
            lista.append(login)
    return lista
    