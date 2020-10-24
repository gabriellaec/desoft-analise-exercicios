def login_disponivel (login, lista_logins):
    login_usuario = ''
    for login in range(len(lista_logins)):
        if login == lista_logins[login]:
            if lista_logins[-1] == '1':
                login_usuario == login + '2'
        else:
            login_usuario = login
    return login_usuario