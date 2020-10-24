def login_disponivel(login, lista_logins):
    if login not in lista_logins:
        return login
    else:
        indice = 1
        for usuario in lista_logins:
            if usuario == login:
                new_login = str(login) + '{}'.format(indice)
                indice += 1
                return new_login