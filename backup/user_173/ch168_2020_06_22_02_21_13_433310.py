def login_disponivel(login,lista):
    for i in lista:
        if login == lista[i]:
            login = lista[i+1]
    return login