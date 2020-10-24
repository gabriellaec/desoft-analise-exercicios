def login_disponivel(login,lista):
    new_login = ""
    for i in range(len(lista)):
        indice = 0
        if login in lista:
            indice +=1
            if int(login[len(login)-1:]) == indice:
                a = int(login[len(login)-1:])
                a+=1
                new_login = login[:len(login)-1] + str(a)
                
            else:
                new_login = login+str(indice)
       
        else:
            new_login = login
            
    return new_login