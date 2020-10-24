from math import sqrt
def encontra_maximo(lista):
    lista_final = []
    for item in lista:
        for subitem in item:
            lista_final.append(subitem)
    if subitem > 0:
        y = max(lista_final)
        return y
    else:
        y = min(lista_final)
        return y
            
        
                