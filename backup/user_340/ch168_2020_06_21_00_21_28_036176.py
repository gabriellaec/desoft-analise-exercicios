def login_disponivel(login,lista):
    m=1
    n=str(m)
    if login not in lista:
        return login
    if login in lista:
        login=login+n
        m+=1
        for nome in lista:
            if login+n==nome:
                login=login+n
        return login
        
        