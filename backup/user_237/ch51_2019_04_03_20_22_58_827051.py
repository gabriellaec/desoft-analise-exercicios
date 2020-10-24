def estritamente_crescente(lista):
    crescente = []
    i = 0
    crescente.append(lista[0])
    for e in lista:
        while crescente[i] < e:
            crescente.append(e)
            i +=1
            
    return crescente
