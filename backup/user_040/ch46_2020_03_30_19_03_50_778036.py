lista = []
def numero_no_indice(x):
    y = 0
    while x[y]<len(x):
        if x[y] == y:
            lista.append(y)
        y+=1
    return lista
        