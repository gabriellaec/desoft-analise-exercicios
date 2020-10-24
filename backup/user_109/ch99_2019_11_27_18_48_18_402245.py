def login_disponivel(login, logins_usandos):
    if login not in logins_usandos:
        return login
    else:
        login = login+"1"
        return login