def numero_no_indice(n):
    lista = []
    for a in n:
        if a == n.index(a):
            lista.append(a)

    return lista