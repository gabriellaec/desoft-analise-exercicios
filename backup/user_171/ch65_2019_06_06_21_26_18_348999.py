def acha_bigramas(string):
    lista=[]
    for e in string:
        b=string[e]+string[e+1]
        if b not in lista:
            lista.append(b)
    return lista