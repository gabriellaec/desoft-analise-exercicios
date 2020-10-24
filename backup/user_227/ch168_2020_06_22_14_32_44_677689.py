def login_disponivel(login, lista):
    numero = 1
    login_inicial = login
    for string in lista:
        if login == string:
            login = login_inicial
            login+=numero
            numero+=1
    
    return login