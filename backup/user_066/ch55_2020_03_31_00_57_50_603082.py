def encontra_maximo(matriz):
    maximo = (matriz[0])[0]
    for i in matriz:
        for j in i:
            if j >maximo:
                maximo = j
    return maximo