def estritamente_crescente(lista):
    cresce = []
    i = 1
    while i < len(lista):
        if lista[i-1]>lista[i]:
            break
        cresce.append(lista[i])
        i+=1
    return cresce
