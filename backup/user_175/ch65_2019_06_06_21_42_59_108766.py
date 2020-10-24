def acha_bigramas(x):
    lista = []
    for i in range(len(x)-1):
        bigrama = x[i] + x[i+1]
        if bigrama not in lista:
            lista.append(bigrama)
    return lista