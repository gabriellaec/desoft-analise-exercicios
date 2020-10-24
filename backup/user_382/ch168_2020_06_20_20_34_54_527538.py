def login_disponivel(login,lista):
    cont = 1 
    while True:
        if login in lista:
            return login
        else:
            login += '{}'.format(cont)
            cont += 1
        
    