def login_disponivel(login,listadelogins):
    lista=listadelogins
    listasemnumero = []
    numero='1,2,3,4,5,6,7,8,9'
    n=0
    for i in lista:
        listasemnumero.append(i.rstrip(numero))

    if login not in lista:
        lista.append(login)
    else:
        n=listasemnumero.count(login)
        lista.append(login+str(n+1))
    return (login+str(n+1))    

