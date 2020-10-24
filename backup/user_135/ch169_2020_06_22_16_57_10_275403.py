def login_disponivel(login, lista_logins):
    login_colocado = login
    if login not in lista_logins:
        lista_logins.append(login)
        return login, lista_logins
    else:
        indice = 1
        while True:
            login = login_colocado + str(indice)
            if login in lista_logins:
                indice += 1
            else:
                break
        return login, lista_logins

lista_logins = []
while True:
    login = str(input())
    login, lista_logins = login_disponivel(login, lista_logins)
    if login == 'fim':
        break

print(lista_logins)
    