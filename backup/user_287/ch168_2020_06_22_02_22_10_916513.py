def login_disponivel(nome_login, lista_usuarios):
    for i in range(len(lista_usuarios)):
        if nome_login in lista_usuarios:
            i +=1 
            return nome_login + '1'
        else :
            return nome_login
 
        