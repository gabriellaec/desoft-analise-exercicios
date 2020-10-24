def estritamente_crescente(lista):
    a = len(lista)
    listo = []
    listo.append(lista[0])
    for i in range(1, a):
        if lista[i] < lista[i + 1] and lista [i] > lista [i-1]:
            listo.append(lista[i])
    return listo
        
    