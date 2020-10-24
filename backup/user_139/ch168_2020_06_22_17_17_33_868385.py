def login_disponivel (login, lista):
    if login not in lista:
        return login
    else:
        for nome in range(len(lista)):
            i = 1
            while login in lista:
                login = login + str(i)
                if login in lista:
                    login = login[:-1]
                i += 1
            return login