def numero_no_indice(n):
    lista = []
    i = 0
    while i< len(n):
        if i == n[i]:
            lista.append(n)
        i += 1
    return lista