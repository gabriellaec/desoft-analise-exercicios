def estritamente_crescente(lista):
    i = 1
    lista_crescente = []
    if len(lista) > 0:
        lista_crescente[0] = lista[0]
        z = 0
    while i < len(lista):
        if lista[i] > lista_crescente[z]:
            lista_crescente.append(lista[i])
            z += 1
        i += 1
    return lista_crescente