import math
def encontra_maximo(lista):
    lista2 = []
    for e in lista:
        for a in e:
        lista2.append(max(abs(a)))
        
    return max(lista2)
        
    
    
    
    
    
    
    
  