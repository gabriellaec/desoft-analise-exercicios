def login_disponivel(nome, lista):
    e = "1"
    for i in lista:
        if nome in lista:
            a = nome+e
            while a in lista:
                l = int(e)
                l+=1
                e = "{}".format(l)
                a = nome+e
        else:
            a = nome
    return a