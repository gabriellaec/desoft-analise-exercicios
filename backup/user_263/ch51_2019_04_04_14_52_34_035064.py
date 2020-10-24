def estritamente_crescente(lista):
    crescente=[lista[0]]
    i=1
    maior=lista[0]
    while i<len(lista):
        if lista[i]>maior:
            crescente.append(lista[i])
            maior=lista[i]
        i+=1
    return crescente