def login_disponivel (login,lista):
    if login not in lista:
        return login
    else:
        for login1 in range(len(lista)):
            i = 1
            while login in lista:
                login = login + str(i)
                i+=1
            return login
                
            
            
