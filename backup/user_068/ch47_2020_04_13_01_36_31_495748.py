def estritamente_crescente(lista):
    a = lista[0]
    i=1
    b = [a]
    while i < len(lista):
        if a < lista[i] and lista[i] < lista[i+1]:
            b.append(lista[i+1])
    i +=1
            
    return b
        
        
   