def encontra_maximo(matriz):
    maior = matriz[0][0]
    i=0
    while i < 3:
        j=0
        a = matriz[i][j]
        while j < 3:
            a = matriz[i][j]
            if a > maior:
                maior = a
            else:
                maior = maior
            j += 1
        i+=1
    return maior