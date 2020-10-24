def encontra_maximo(matriz):
    a = 0

    maximo = 0
    while a < 3:
        b = 0
        while b < 3:
            
            if matriz[a][b] > maximo:
                maximo = matriz[a][b]   
            
            b += 1
        
        a += 1
    
    return maximo