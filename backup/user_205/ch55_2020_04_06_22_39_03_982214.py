from math import sqrt
def encontra_maximo(lista):
    lista_final = []
    for item in lista:
        for subitem in item:
            lista_final.append(sqrt(subitem**2))
    print (lista_final)
    return max(lista_final)
    
    
            
        
                