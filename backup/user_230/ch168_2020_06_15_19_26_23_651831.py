def login_disponivel(login, lista):
    if login not in lista:
        lista.append(login)
    else:
        lista.append(login+"1")
    return lista