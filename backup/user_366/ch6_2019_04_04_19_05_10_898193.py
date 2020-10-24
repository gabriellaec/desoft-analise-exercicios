def encontra_maximo(matriz):
    maior = matriz[0][0]
    for e in matriz:
        for k in e:
            if m > maior:
                maior = k
    return maior