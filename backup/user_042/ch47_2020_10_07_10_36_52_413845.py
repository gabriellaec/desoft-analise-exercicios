def estritamente_crescente (lista):
    if len(lista) == 0:
        return lista
    i = 1
    lista_nova = [0]
    lista_nova[0] = lista[0]
    m = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > m:
            lista_nova.append(lista[i])
            m = x[i]
        i += 1
    return lista_nova