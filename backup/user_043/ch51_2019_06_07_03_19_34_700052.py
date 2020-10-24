def estritamente_crescente(lista):
    crescente = []
    maxim = 0
    i = 0
    while i< len(lista):
        if lista[i] > maxim:
            maxim = lista[i]
            crescente.append(maxim)
        i +=1
    return crescente