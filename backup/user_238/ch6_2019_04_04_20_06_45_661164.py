def encontra_maximo(matriz):
    maior=0
    for listas in matriz:
        for numeros in listas:
            if numeros>maior:
                maior=numeros
    return maior
matriz=[[1, 2, 3], [4, -5, 6], [7, 8, 9]]
print(encontra_maximo(matriz))
