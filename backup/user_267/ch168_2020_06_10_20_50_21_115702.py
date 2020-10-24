def login_disponivel(login, lista_logins):
    i = 1
    if login not in lista_logins:
        return login
    else:
        return lista_logins[login] + "i"
        