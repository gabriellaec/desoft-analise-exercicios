def encontra_maximo(matriz):
    x=matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<0:
                matriz[i][j]= (-matriz[i][j])
            elif matriz[i][j]>x:
                x=matriz[i][j]
    return x
        