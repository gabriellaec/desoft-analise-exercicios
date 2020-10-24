def login_disponivel(login,lista):
    c = 1
    for i in lista:
        if login not in lista:
            lista.append(login)
        else:
            lista.append(login + str(c))
            c +=1 
    return lista