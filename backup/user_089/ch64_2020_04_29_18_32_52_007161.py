def acha_bigramas(x):
    lista = []
    i = 0
    while i < len(x):
        z = x[i:i+2]
        if z not in lista and len(z) == 2:
            lista.append(z)
            i += 1       
        else:
            i += 1
    return lista