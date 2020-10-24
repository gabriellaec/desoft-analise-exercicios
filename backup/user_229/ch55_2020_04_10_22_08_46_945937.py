def encontra_maximo(matriz):
    oi = matriz[0]
    maior = oi[0]
    for i in range(1,len(matriz)):
        a = matriz[i]
        for l in range(1,len(matriz[i])):
            if a[l] > a[l-1]:
                if a[l] > maior:
                    maior = a[l]
    return maior
