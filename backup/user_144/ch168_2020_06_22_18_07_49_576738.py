def login_disponivel(login,lista):
    new_login = ""
    for i in range(len(lista)):
        indice = 0
        if login in lista:
            indice +=1
            new_login = login+str(indice)
            
        else:
            new_login = login
            
    return new_login