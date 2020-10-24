def login_disponivel(login,lista):
    teste = True
    usuario = login
    i = 1
    while teste:
        if usuario in lista:
            usuario = login + '{0}'.format(i)
            i += 1
        else:
            break
    return usuario