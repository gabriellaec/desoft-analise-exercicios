def acha_bigramas(x):
    lista = []
    i = 0
    u = 1
    while u < len(x):
        if x[i] + x[u] in lista:
            pass
        else:
            lista.append(x[i] + x[u])
        i += 1
        u += 1
    return lista