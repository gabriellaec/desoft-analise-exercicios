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
                contador = 1
                while condicao:
                    users = lista_logins[i]
                    if users[:len(users)] == login:
                        i += 1
                        contador += 1
                    else:
                        contador = str(contador)
                        condicao = False
                        verifica = False
                        return login + contador                       
            else:
                i += 1