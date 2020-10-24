def encontra_maximo(matriz):
    maior = 0
    for lista in matriz:
        for e in lista:
            if abs(e) > maior:
                maior = abs(e)
    return maior
         
        
        
    
    