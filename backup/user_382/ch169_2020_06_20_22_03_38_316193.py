def login_disponivel(login,lista):
    cont = 1 
    new_login = login 
    while True:
        if new_login not in lista:
            return new_login
        else:
            new_login = login + '{}'.format(cont)
            cont += 1
            
lista_login = []
while True:            
    login = input()
    if login == 'fim':
        break 
    else:
        new_login = login_disponivel(login,lista_login)
        lista_login.append(new_login)
    print(new_login)
