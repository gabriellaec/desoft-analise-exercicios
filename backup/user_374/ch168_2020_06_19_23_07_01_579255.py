def login_disponivel(login, lista_login):
    nome_login = login
    contador = 0
    x = True
    
    while x:
        if nome_login not in lista_login:
            return nome_login
            x = False
        else:
            contador += 1
            nome_login = login + str(contador)