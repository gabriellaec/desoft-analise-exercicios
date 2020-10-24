def login_disponivel(login,lista_registros):
    i= 1
    usuario = login  
    for nome in lista_registros:
        if login == nome:
            login = usuario + str(i)
            i+=1
    return login
