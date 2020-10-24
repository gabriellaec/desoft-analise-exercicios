def login_disponivel(login,lista_login):
    login_novo = []
    if login in lista_login:
        login_novo = login + '1'
        return login_novo
    else:
        return login
        
    