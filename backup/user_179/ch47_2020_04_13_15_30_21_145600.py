def estritamente_crescente (lista):
    crescente = []
    crescente.append(lista[0])
    i = 0
    while i < (len(lista)-1):
        if lista[i+1] > lista[i]:
            crescente.append(lista[i+1])
            i += 1
        else:
            i += 1
    return crescente