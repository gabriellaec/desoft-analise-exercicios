def login_disponivel(nome_login, lista_usuarios):
    i = 0
    if nome_login in lista_usuarios:
        i +=1 
        return nome_login + ('1' or '2')
    else :
        return nome_login
        