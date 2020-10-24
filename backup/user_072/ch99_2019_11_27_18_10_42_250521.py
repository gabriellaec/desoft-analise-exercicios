def login_disponivel(login, lista):
    for i in lista:
        if login == lista[i]:
            return login + i
        else:
            return login
print(login_disponivel(login, lista))