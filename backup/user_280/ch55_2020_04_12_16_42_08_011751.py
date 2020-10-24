def encontra_maximo(matriz):
    i=0
    j=0
    a = matriz[i][j]
    maior = a
    while i < 4:
        while j < 4:
            if a > maior:
                maior = a
            else:
                maior = maior
            j += 1
        i+=1
    return maior