def login_disponivel(login, lista):
    i = 1
    for e in lista:
        if login == e:
            i = str(i)
            lista.append(login + i)
            i = int(i)
            i += 1
        else: 
            lista.append(login)
    return lista
    