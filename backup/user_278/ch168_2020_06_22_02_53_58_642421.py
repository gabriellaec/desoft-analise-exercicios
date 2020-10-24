def login_disponivel(login,lista):
    if login not in lista:
        return login
    else:
        num = 1
        if login+str(num) not in login:
            return login+str(num)
        else:
            num+=1