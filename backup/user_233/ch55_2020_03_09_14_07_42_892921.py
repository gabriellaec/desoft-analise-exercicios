def encontra_maximo(matriz):
    
    maximo = 0
    
    for linha in matriz:
        for item in linha:
            if item < 0: item = -item
            if item > maximo: maximo = item
    
    return maximo