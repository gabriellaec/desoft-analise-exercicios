def login_disponivel (login,lista):
    if login not in lista:
        return login
    números = ['0','1','2','3','4','5','6','7','8','9']
    if login in lista:
        último_caracter = login[-1]
        if último_caracter not in números:
            novo_login = login + "1"
        else:
            novo_digito = int(último_caracter) + 1
            novo_login = login + str(novo_digito)
        return novo_login