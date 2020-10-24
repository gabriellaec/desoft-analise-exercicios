def acha_biagramas(string):
    lista=[]
    for e in string:
        b=string[e]+string[e+1]
        if  not in lista:
            lista.append(b)
    return lista