def encontra_maximo(matriz):
    maximo = matriz[0][0]
    for c in matriz:
        for i in c:
            if i > maximo:
                maximo = i
    return maximo
