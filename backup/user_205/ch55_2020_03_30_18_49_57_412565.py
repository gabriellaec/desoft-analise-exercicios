def encontra_maximo(lista):
    for item in lista:
        for subitem in item:
            y = max(subitem, key=int)
    return y
            
        
                