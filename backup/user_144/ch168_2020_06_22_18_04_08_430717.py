def login_disponivel(login,lista):
    new_login = ""
    indice = 0
    for i in range(len(lista)):
        if login not in lista[i]:
            new_login = login
            
        else:
            indice+=1
            new_login = login+str(indice)
            
    return new_login