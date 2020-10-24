def login_disponivel(login, lista):
    novo_login=0
    if login not in lista:
        lista.append(login)
    else:
        lista.append(login+"1")
        novo_login=login+"1"
    return novo_login