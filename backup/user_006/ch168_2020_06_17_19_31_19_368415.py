def login_disponivel(login, lista):
    i=0
    e=1
    while i<len(lista):
        if login not in lista:
            return login
        else:
            login=login+str(e)
        e=e+1
        i=i+1   
    