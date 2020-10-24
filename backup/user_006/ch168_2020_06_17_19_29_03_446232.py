def login_disponivel(login, lista):
    i=0
    e=1
    while i<len(lista):
        if login is not in lista:
            return login
        else:
            login=login+e
        e=e+1
        i=i+1   
    