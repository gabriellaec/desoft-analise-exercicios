def login_disponivel(username,lista):
    if username not in lista:
        return username
    else:
        n = 1
        new_username = username + str(n)
        trying = True
        while trying:
            if new_username not in lista:
                return new_username
            else:
                n += 1
                new_username = username + str(n)

lista_login = []
listando = True
while listando:
    login = input("Log in: ")
    if login == 'fim':
        listando = False
    else:
        disponivel = login_disponivel(login,lista_login)
        lista_login.append(disponivel)
for login in lista_login:
    print(login)
