fim = True
def login_disponivel(usuario, lista):
    i = 1
    login = usuario
    for nome in lista:
        if login == nome:
            login = usuario + str(i)
            i += 1
    return login