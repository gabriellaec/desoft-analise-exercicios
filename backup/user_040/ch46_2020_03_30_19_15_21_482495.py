lista = []
def numero_no_indice(x):
    y = 0
    número = x[y]
    while y<len(x):
        if número == y:
            lista.append(número)
        y+=1
    return lista
        