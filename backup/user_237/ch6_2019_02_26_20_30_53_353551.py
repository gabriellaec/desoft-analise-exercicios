import math
def encontra_maximo(lista):
    lista2 = []
    for e in lista:
        lista2.append(max(math.abs(e)))
        
    return max(lista2)
        
    
    
    
    
    
    
    
  