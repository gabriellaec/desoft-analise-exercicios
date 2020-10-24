def login_disponivel(login, lista_logins):
    if login not in lista_logins:
        return login
    else:
        i = 0
        contador = 0
        while i < len(lista_logins):
            user = lista_logins[i]
            if user[:len(user)] == login:
                i += 1
                contador += 1
            i += 1
        contador = str(contador)
        return login + contador
