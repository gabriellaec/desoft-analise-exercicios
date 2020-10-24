def login_disponivel(login, lista):
    i = 1
    for e in lista:
        if login == e:
            login = login + str(i)
            lista.append(login)
            i += 1
        else:
            lista.append(login)
    return lista