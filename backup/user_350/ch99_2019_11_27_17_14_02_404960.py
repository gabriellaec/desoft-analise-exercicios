def login_disponivel(login,lista):
    c = 1
    for i in lista:
        if login not in lista:
            login = login
        else:
            login =  login + str(c)
        	c +=1
        return login 
            