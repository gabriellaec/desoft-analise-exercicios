from math import sqrt
def encontra_maximo(lista):
    lista_final = []
    for item in lista:
        for subitem in item:
            lista_final.append(subitem)
    return max(|lista_final|)
    
    
            
        
                