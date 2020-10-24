def encontra_maximo(matriz):
    maior= 0 
    for i in matriz:
        if i > maior:
            maior=i
    return maior