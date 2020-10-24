def numero_no_indice(x):
    lista = []
    y=0
    while y < len(x):
        if x[y] == x.index(x[y]):
            lista.append(y)
        y +=1
    return lista
        