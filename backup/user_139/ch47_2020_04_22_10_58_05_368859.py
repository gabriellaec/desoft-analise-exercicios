def estritamente_crescente(lista):
    lista2 = []
    i = 1
    n = lista[0]
    while i < len(lista):
        if n < lista [i]:
            lista2.append(lista[i])
            n = lista [i]
            i += 1
        else:
            i += 1
    return lista2