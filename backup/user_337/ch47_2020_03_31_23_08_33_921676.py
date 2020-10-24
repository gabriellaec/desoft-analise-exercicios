def estritamente_crescente(lista):
    for i in range(len(lista)):
        if lista[i] < lista[i-1]:
            del lista[i]
    return lista