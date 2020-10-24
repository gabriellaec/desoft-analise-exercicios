def login_disponivel(login,lista):
    m=1
    n=str(m)
    if login not in lista:
        return login
    if login in lista:
        for i in lista:
            if login+n in lista:
                m+=1
                login=login+n
                return login
        
        