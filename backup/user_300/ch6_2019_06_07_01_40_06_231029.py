def al(lista):
    return len(lista)
def encontra_maximo(lista):
    x = 0
    j = al(lista)
    for a in range(j):
        for b in range(j):
            if lista1[a][b] > x:
                x = lista1[a][b]
                
    for a in range(0,j,-1):
        for b in range(0,j,-1):
            if lista1[a][b] > x:
                x = lista1[a][b]
    
    
    return x