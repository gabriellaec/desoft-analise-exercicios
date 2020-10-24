def encontra_maximo(matriz):
    lista=[]
    for i in range(0, rows):
        for j in range(0, cols):
            lista.append(matriz[i][j])
    return max(lista)