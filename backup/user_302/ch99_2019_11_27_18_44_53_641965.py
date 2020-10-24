def login_disponivel(login, lista_logins):
    a = 1
    login_disponivel = login
    while login_disponivel in lista_logins:
        b = a
        login_disponivel = login + str(b)
        a += 1
    else:
        login_disponivel = login
    return login_disponivel