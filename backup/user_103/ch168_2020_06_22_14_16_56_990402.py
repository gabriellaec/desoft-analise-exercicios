def login_disponivel(login,lista_registros):
    i= 1
    for nome in lista_registros:
        if login == nome:
            login = nome + str(i)
            i+=1
    return login


