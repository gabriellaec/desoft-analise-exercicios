def estritamente_crescente (lista):
    i = 0
    crescente = []
    while i < (len(lista)-1):
        if lista[i+1] > lista[i]:
            crescente.append(lista[i])
            i += 1
        else:
            i += 1
    return crescente