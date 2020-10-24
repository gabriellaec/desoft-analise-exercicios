def numero_no_indice(l1):
    lista = []
    for i in l1:
        if i == l1.index(i):
            lista.append(i)
        return lista