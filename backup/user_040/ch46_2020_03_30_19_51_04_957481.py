lista = []
def numero_no_indice(x):
    for y in range(len(x)):
        if x[y] == x.index(x[y]):
            lista.append(y)
    return lista
        