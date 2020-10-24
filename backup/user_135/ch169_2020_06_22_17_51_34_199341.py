def login_disponivel(login, lista_logins):
    login_colocado = login
    if login not in lista_logins:
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

lista = []
while True:
    login = str(input())
    if login == 'fim':
        break
    else:
        lista.append(login_disponivel(login, lista))
del lista[-1]
print(lista)