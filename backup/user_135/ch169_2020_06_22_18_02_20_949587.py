def login_disponivel(login, lista_logins):
    login_colocado = login
    if login not in lista_logins:
        return login
    else:
        indice = 1
        while True:
            if login in lista_logins:
                login = login_colocado + str(indice)
                indice += 1
            else:
                return login

lista = []
while True:
    login = login_disponivel(str(input()), lista[])
    if login == 'fim':
        break
    lista.append(usuario)

print(lista)