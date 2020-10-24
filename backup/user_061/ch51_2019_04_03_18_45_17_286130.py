def estritamente_crescente(lista):
    cresce = [lista[0]]
    i = 0
    while i < len(lista):
        if lista[i-1]<lista[i]:
            cresce.append(lista[i])
        i+=1
        
    return cresce

