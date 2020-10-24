def estritamente_crescente(lista1):
    lista2 = []
    lista2.append(lista1[0])
    i = 1
    while i < len (lista1):
        if lista1[i] > lista2 [i-1]:
            lista2.append(lista1[i])
        i += 1
    return lista2
        