def encontra_maximo(lista):
    x = -999999999999
    j = len(lista)
    
    for a in range(j):
        for b in range(len(lista[a])):
            if lista[a][b] > x:
                x = lista[a][b]
                
    for a in range(0,j,-1):
        for b in range(0,len(lista[a]),-1):
            if lista[a][b] > x:
                x = lista[a][b]
    
    return x