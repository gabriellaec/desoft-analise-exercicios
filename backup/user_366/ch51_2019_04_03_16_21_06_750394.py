def estritamente_crescente(lista):
    new = []
    new[0] = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > lista[i-1]:
            new.append(lista[i])
        else:
            i += 1
    return new