def zera_negativos(x):
    i = 0
    lista=[]
    while i<len(x):
        if x[i] < 0:
            lista.append(0)
        if x[i] >= 0:
            lista.append(x[i])
        i += 1
    return lista   