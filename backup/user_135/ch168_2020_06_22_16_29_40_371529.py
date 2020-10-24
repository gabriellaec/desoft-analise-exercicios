def login_disponivel(login, lista_logins):
    if login not in lista_logins:
        lista_logins.append(login)
        return login
    else:
        indice = 1
        for usuario in lista_logins:
            if usuario == login:
                new_login = str(login) + '{}'.format(indice)
                indice += 1
            else:
                return new_login