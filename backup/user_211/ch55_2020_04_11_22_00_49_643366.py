def encontra_maximo(matriz):
    lista=[]
    for i in range(0,3):
        for j in range(0,3):
            lista.append(matriz[i][j])
    return max(abs(lista))