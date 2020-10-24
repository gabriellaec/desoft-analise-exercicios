def encontra_maximo(matriz):
    oi = matriz[0]
    maior = oi[0]
    for i in range(len(matriz)):
        a = matriz[i]
        for l in range(len(matriz[i])):
            if a[l] > a[l-1]:
                if abs(a[l]) > maior:
                    maior = a[l]
    return maior