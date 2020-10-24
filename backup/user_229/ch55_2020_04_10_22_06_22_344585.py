def encontra_maximo(matriz):
    maior = 0
    for i in range(len(matriz)):
        a = matriz[i]
        for l in range(len(matriz[i])):
            if a[l] > a[l-1]:
                if a[l] > maior:
                    maior = a[l]
    return maior