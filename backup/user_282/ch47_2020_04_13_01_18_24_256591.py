def estritamente_crescente(lista):
    count = 0
    saida = list()
    for e in range(len(lista)):
        if lista[e] > count:
            saida.append(lista[e])
            count = lista[e]
    return saida