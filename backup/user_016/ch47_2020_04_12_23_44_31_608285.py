def estritamente_crescente(lista1):
    lista2 = []
    lista2.append(lista1[0])
    i = 1
    while i < len(lista1):
        if lista1[i] > max(lista2):
            lista2.append(lista1[i])
        else:
            pass
        i += 1
    return lista2