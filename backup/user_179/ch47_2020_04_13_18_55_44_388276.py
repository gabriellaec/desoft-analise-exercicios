def estritamente_crescente (lista):
    crescente = []
    i = 0
    maior = lista[0]
    while i < (len(lista)-1):
        if lista[i+1] > maior:
            crescente.append(lista[i+1])
            maior = lista[i+1]
            i += 1
        else:
            i += 1
    return crescente