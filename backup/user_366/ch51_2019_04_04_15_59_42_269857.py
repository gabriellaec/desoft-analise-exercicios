def estritamente_crescente(lista):
    new = [0]
    new[0] = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] in new:
            i += 1
        else:
            if lista[i] > lista[i-1]:
                new.append(lista[i])
                i += 1
            else:
                i += 1
    return new