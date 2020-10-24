def acha_bigramas(a):
    lista = list()
    for i in range(2,len(a)+1):
        b = a[i-2:i]
        if b not in lista:
            lista.append(b)


    return lista