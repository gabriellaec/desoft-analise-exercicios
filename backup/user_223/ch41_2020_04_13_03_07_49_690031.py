def zera_negativos(lista):
    newlist=[]
    for e in lista:
        if e<0:
            newlist.append(0)
        else:
            newlist.append(e)
    return newlist