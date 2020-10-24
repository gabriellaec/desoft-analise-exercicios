def login_disponivel(login,lis_login):
    cont = 1
    x = login
    for i in lis_login:
        if i == x:
            numero = str(cont)
            x = login + numero
            cont +=1
    return x