def login_disponivel(login,lista):
    while True:
        if login in lista:
            return login
        else:
        login += '{}'.format(cont)
        cont += 1
        
    