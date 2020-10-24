def zera_negativos(x):
    i = 0
    lista_nova = []
    while i < len(x):
        if x[i] < 0:
            lista_nova.append(0)
        else:
            lista_nova.append(x[i])
        i += 1
    return lista_nova