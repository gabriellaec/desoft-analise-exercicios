def login_disponivel (login, lista):
    if login not in lista:
        return login
    else:
        soma = 0
        for i in lista:
            if i[:len(login)] == login:
                soma += 1
        return login + "{}".format(soma)