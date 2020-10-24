def estritamente_crescente(lista):
    i=1
    j=0
    somente_crescente=[lista[0]]
    while i<len(lista):
        if int(lista[i])>int(somente_crescente[j]):
            somente_crescente.append(lista[i])
            j+=1
        i+=1
    return somente_crescente


lista=[50,70,80,80,40,100]

print(estritamente_crescente(lista))


