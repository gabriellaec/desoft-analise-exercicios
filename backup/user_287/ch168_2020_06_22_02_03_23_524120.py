def login_disponivel(nome_login, lista_usuarios):
    if nome_login in lista_usuarios:
        return nome_login + '1'
    else :
        return nome_login
        