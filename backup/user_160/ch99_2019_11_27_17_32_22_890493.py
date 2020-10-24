def login_disponível(login,lista):
    i = 1
    if login not in lista:
        return (login)
    while login in lista:
        login = login*(i)
        i += 1
    return (login)
        
   