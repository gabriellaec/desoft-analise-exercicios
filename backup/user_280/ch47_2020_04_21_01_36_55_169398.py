def estritamente_crescente(lista):
    lista2 = lista[0]
    i=1
    while i < len(lista):
        if lista[i] > lista2[-1]:
            lista2.append(lista[i+1])
        i += 1
    return lista2
        