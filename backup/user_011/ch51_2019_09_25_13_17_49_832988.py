def estritamente_crescente(lista):
    l_crescente = []
    i = 1
    while i < len(lista):
        if lista[i] > lista[i-1]:
            l_crescente.append(lista[i])
        i += 1
    return l_crescente