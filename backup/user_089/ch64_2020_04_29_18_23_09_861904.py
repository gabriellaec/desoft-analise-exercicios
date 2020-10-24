def acha_bigramas(x):
    lista = []
    for e in x:
        z = x[e:e+2]
        if z not in lista:
            lista.append(z)
    return lista