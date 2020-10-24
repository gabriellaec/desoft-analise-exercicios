def login_disponivel(login,lista):
    for i in lista:
        if login not in lista:
            return login
        else:
            contador = 0
            for nome in lista:
                if nome[0:len(login)] == login:
                    contador += 1
            return login + str(contador)