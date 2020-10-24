def login_disponivel(login, logins_usandos):
    if login not in logins_usandos:
        return login
    else:
        i = 1
        while True:
            login = login+"i"
            if login not in logins_usandos:
                return login
            else:
                login = login + "i"
                i += 1