def acha_bigramas (string):
    i=1
    lista=[]
    bi=0
    while i<len(string):
        b = string[i-1]
        e=string[i]
        bi = b+e
        if bi not in lista:
            lista.append(bi)
        i+=1
    return lista