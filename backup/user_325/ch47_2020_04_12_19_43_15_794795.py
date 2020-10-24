def estritamente_crescente(lista):
    lista2 = []
    i = 0
    s = 0
    while i < len(lista):
        if lista[s+1] > lista[s]:
            lista2.append(lista[s])
        i += 1
    return lista2
        