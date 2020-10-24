def estritamente_crescente(lista1):
    n = len(lista1)
    i = 1
    x = 0
    lista2 = [lista1[0]]
    while i < n:
        if lista2[x] < lista1[i]:
            lista2.append(lista1[i])
            i += 1
            x += 1
        else:
            i += 1
    return lista2