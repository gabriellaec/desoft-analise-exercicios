def estritamente_crescente (lista):
    i = 0 
    r = 0
    lista2 = [lista[0]]
    while i < len(lista):
        if lista [i] > lista2 [r]:
            lista2.append(lista[i])
            i += 1
            r += 1
        else:
            i += 1
    return lista2