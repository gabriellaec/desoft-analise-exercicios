def estritamente_crescente(lista):
    for i in range(len(lista)):
        if lista[i+1] < lista[i]:
            del lista[i+1]
    return lista