def filtra_positivos(lista5):
    
    i = 0
    
    lista7 = []
    
    while i < len(lista5):
        
        if lista5[i] >= 0:
            
            lista7.append(lista5[i])
            
        i += 1 
        
    return lista7

aaa = [-1, -2, -3, 0, 1, 2]

print(filtra_positivos(aaa))
      