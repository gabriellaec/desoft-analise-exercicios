def login_disponivel(nome_login, lista_usuarios):
    i = 0
    if nome_login in lista_usuarios:
        i +=1 
        return nome_login + 'i'
    else :
        return nome_login
        