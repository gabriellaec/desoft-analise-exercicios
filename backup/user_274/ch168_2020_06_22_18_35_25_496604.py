def login_disponivel(login, lista):
    c = 0
    for i in lista:
        if i[:len(login)] == login:
             c = c+1
             
    if c > 0:
        return login+str(c)
    else:
        return login