def acha_bigramas(x):
    lista = []
    i = 0
    j=1
    while i<len(x):
        lista.append(x[i,j])
        i+=1
        j+=1
    return lista