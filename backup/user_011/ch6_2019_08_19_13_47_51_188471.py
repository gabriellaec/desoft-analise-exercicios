def encontra_maximo(lista):
    
    for e in lista[0]:
        x = max(lista[0])
    for e in lista[1]:
        y =max(lista[1])
    for e in lista[2]:
        z = max(lista[2])
            
    if x > y and x > z:
            return x
    elif y > x and y > z:
            return y 
    else:
            return z
         
        
        
    
    