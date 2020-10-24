def login_disponivel(login,lista):
    c = 1
    for i in lista:
        if login not in lista:
            return login 
        else:
            return login + str(c)
        	c +=1 