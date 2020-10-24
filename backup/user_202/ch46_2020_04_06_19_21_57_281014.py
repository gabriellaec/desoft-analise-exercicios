def numero_no_indice(x):
    a = 0
    lista = []
    for i in x:
        if i == a:
            lista.append(i)
        a += 1
    return lista
        