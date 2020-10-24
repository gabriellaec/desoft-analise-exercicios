def login_disponivel(login,lista):
    if login not in lista:
        return login
    else:
        i = 1
        while True:
            nome = login + str(i)
            if nome not in lista:
                return nome
            else:
                i += 1