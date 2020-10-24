lista = []

def zera_negativos (lista):
    i = 0
    
    while i < len (lista):
        
        while lista [i] < 0:
            lista [i] = 0
            
        i += 1
    return lista
