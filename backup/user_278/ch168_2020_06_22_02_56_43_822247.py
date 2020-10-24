def login_disponivel(login,lista):
    if login not in lista:
        return login
    else:
        num = 1
        while True:
            if login+str(num) not in lista:
                return login+str(num)
            else:
                num+=1