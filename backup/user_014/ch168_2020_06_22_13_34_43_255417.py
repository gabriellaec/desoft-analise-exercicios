def login_disponivel (login, lista_logins):
    login_usuario = ''
    for i in lista_logins:
        if login == lista_logins[i]:
            if lista_logins[i][-1] == '1':
                login_usuario == login + '2'
        else:
            login_usuario = login
    return login_usuario