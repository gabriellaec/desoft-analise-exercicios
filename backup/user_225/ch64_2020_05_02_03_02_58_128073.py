def acha_bigramas(string):
    i = 1
    lista = []
    while i < len(string):
        b = (string[i-1]+string[i])
        if b not in lista:
             lista.append(b)
        i+=1
    return lista