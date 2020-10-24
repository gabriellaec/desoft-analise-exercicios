def login_disponivel(login, lista_logins):
    if login not in lista_logins:
        return login
    else:
        verifica = True
        i = 0
        while verifica:
            
            condicao = True
            users = lista_logins[i]
            if users == login:
                contador = 0
                while condicao:
                    users = lista_logins[i]
                    if users[:len(users)-1] == login:
                        i += 1
                        contador += 1
                    else:
                        contador = str(contador)
                        return login + contador
                        condicao = False
                        verifica = False
            else:
                i += 1