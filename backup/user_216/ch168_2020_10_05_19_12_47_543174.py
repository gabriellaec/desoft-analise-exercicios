def login_disponivel(login,lista):
    teste = True
    i = 1
    while teste:
        if login in lista:
            login = login + '{0}'.format(i)
            i += 1
        else:
            break
    return login