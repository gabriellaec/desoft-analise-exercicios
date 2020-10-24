def encontra_maximo(matriz):
    x=matriz[0][0]
    if x<0:
        x=-x
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<0:
                matriz[i][j]= -(matriz[i][j])
            if matriz[i][j]>x:
                x=matriz[i][j]
    return x