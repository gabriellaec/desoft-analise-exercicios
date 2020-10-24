def encontra_maximo(matriz):
    maximo=matriz[0][0]
    i=0
    while i<3:
        j=0
        while j<3:
            if maximo<matriz[i][j]:
                maximo=matriz[i][j]
            j=j+1
        i=i+1
    if maximo<0:
        maximo=maximo-(maximo*2)
    
    return maximo