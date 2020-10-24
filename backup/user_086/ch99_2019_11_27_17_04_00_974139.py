#login é uma string e lista é uma lista de logins, logom, strings também
def login_disponivel(login,lista):
    if login in lista:
        i = 1
        while login+str(i) in lista:
            i+=1
        if not login+str(i) in lista:
            return login+str(i)
    else:
        return login