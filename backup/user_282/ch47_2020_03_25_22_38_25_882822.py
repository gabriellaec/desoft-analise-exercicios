def estritamente_crescente(lista):
    lista1 = []
    i = 1
    lista1.append(lista[0])
    while i<len(lista):
        if lista[i]>lista[i-1]:
            lista1.append(lista[i])
        i += 1
    else:
        return(lista1)