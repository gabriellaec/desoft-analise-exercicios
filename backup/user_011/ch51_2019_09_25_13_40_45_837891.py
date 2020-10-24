def estritamente_crescente(lista):
    l_crescente = [lista[0]]
    i = 1
    n = lista[0]
    while i < len(lista):
        if lista[i] > n:
            n = lista[i]
            l_crescente.append(n)
        i += 1
    return l_crescente