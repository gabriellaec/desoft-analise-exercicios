def acha_bigramas (string):
    i=1
    lista=[]
    bi=0
    while i<len(string):
        b = string[i-1]
        i=string[i]
        bi = b+i
        if bi not in lista:
            lista.append(bi)
        i+=1
    return lista