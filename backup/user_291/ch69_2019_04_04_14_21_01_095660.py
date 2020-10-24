def junta_listas(lista):
    
    lista2 = []
    
    i = 0
    
    t = 0
    
    while i < len(lista):
        
        while t < len(lista[i]):
            
            lista2.append(lista[i][t])
            
            t += 1
        
        t = 0
        
        i += 1
    
    return lista2
    
    