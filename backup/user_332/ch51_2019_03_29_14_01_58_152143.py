def estritamente_crescente (lista):
    maior = lista[0]
    
    lista2 = []
    
    lista2.append(lista[0])
    
    for i in lista:
        
        if (lista[i] > maior):
            lista2.append(lista[i])
            maior = lista[i]
            
    return(lista2)