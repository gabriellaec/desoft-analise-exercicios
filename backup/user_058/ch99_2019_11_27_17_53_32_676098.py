def login_disponivel(login,logins):
    novo_login = login
    i = 1
    while novo_login in logins:
        novo_login = "{0}{1}".format(login,i)
        i += 1
    return novo_login