def soma_impares (lista):
    si = 0
    i = 0
    while i < len(lista):           
        if lista [i] %2 != 0:
            si += lista [i]
        i += 1    
             
        return si
        