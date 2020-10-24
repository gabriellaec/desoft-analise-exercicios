def encontra_maximo(matriz):
    oi = matriz[0]
    maior = oi[0]
    for i in range(len(matriz)):
        a = matriz[i]
        for l in range(len(a)):
            if abs(a[l]) > abs(a[l-1]):
                if abs(a[l]) > maior:
                    maior = abs(a[l])
    return maior