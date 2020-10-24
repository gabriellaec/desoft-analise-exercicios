def estritamente_crescente(lista):
    cresce = []
    i = 0
    while i < len(lista)-1:
        i+=1
        if lista[i-1]<lista[i]:
            cresce.append(lista[i])
    return cresce

