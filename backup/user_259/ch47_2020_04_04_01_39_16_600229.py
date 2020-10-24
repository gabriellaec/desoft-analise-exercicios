def estritamente_crescente(lista):
    crescente = [lista[0]]
    i = 0
    while i<len(lista):
        if len(lista) == 0:
            crescente = []
            break
        if lista[i+1]>lista[i]:
            crescente.append(lista[i+1])
            i+=1
        else:
            break
    return crescente
        
        
        
        
