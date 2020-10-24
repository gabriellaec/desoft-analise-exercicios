def login_disponivel(stri, lista):
    if stri not in lista:
        return stri
    else:
        i=1
        x=stri+str(i)
        while x in lista:
            x=stri+str(i)
            i+=1
        return x