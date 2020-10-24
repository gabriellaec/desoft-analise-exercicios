def numero_no_indice(n):
    lista = []
    l = len(n)
    for i in range(0, l):
        if i == n[i]:
            lista.append(n[i])
    return lista