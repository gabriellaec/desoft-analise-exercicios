def login_disponivel(login,lista):
    cont = 1 
    new_login = login 
    while True:
        if new_login not in lista:
            return login
            break 
        else:
            new_login = login + '{}'.format(cont)
            cont += 1
        
    