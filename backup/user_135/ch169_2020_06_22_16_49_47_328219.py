def login_disponivel(login, lista_logins):
    login_colocado = login
    elif login not in lista_logins:
        lista_logins.append(login)
        return login
    else:
        indice = 1
        while True:
            login = login_colocado + str(indice)
            if login in lista_logins:
                indice += 1
            else:
                break
        return login

lista_logins = []
while login != 'fim':
    login = str(input())
    login_disponivel(login, lista_logins)
    
print(lista_logins)
    