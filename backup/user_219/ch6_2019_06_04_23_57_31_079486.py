def encontra_maximo(matriz):
    maior= matriz[0][0]
    for i in range(0,len(matriz)):
        for a in matriz[i]:
            if a > maior:
                maior=a
    return maior