def acha_bigramas(x):
    lista = []
    i = 0
    while i < len(x):
        if x[i:(i+2)] in lista:
            i += 1
        else:
            lista.append(x[i:(i+2)])
            i += 1
    return lista