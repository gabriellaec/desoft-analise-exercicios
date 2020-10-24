def numero_no_indice(x):
    lista = []
    for t in range(len(x)):
        if t == x[t]:
            lista.append(t)
    return lista