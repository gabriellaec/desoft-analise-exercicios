def encontra_maximo(matriz):
    
    maximo = False
    
    for linha in matriz:
        for item in linha:
            if not maximo: maximo = item
            elif item > maximo: maximo = item
    
    return maximo