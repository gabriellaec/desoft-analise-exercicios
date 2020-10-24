def login_disponivel(login,lista):
    cont = 1 
    while True:
        if login in lista:
            return login
            break 
        else:
            login += '{}'.format(cont)
            cont += 1
        if login not in lista:
            break 
        
    