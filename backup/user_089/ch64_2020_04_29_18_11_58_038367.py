def acha_bigramas(x):
    lista = []
    i = 0
    while i < len(x):
        lista.append(x[i:(i+2)])
        i += 1
    return lista