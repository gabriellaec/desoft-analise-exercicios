def estritamente_crescente(lista):
    crescente=[]
    crescente.append(lista[0])
    i=1
    while(i<len(lista)):
        if lista[i]>lista[i-1] and not lista[i] in crescente:
            crescente.append(lista[i])
        i+=1
    return crescente

print(estritamente_crescente([1, 3, 2, 3, 4, 6, 5]))