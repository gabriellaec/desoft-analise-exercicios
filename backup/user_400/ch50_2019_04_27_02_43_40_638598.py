def numero_no_indice(x):
    i = 0
    lista = []
    while i < len(x):
        if x[i] == i:
            lista.append(x[i])
        i += 1
    return lista