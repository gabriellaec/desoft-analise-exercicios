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

lista = []
while True:
    login = str(input())
    login_disponivel(login, lista)
    if login == 'fim':
        break
del lista[-1]
print(lista)