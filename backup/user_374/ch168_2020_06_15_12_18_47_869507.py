def login_disponivel(login, lista_de_logins):
    contador = 1
    for i in lista_de_logins:
        if (login + str(contador)) == i:
            contador += 1
            
    
    return login + str(contador)
            
