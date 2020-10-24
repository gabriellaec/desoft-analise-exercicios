def zera_negativos(lista2):
    i = 0
    while i < len(lista2):
        
        if lista2[i] < 0:
            lista2[i] = 0
            
        i+=1
    
    return lista2