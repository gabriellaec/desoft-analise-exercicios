def login_disponivel(loginori, lista):
    i=0
    e=1
    login=loginori
    while i<len(lista):
        if login not in lista:
            return login
        else:
            login=loginori+str(e)
        e=e+1
        i=i+1   
    