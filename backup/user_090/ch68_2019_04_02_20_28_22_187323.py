def separa_trios(y):
    lista=[]
    i=0
    while i<len(y):
        lista.append(y[i:i+3])
        i+=3
    lista.append(y[i:len(y)])
    return lista