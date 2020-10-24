def encontra_maximo(matriz):

    i = 0
    p = 0
    q = 0
    r = 0
    maior = matriz[0][0]

    while i < len(matriz):
        if i == 0:
            while p <= 2:
                if matriz[i][p] > maior:
                    maior = matriz[i][p]
                p += 1
        if i == 1:
            while q <= 2:
                if matriz[i][q] > maior:
                    maior = matriz[i][q]
                q += 1
        if i == 2:
            while r <= 2:
                if matriz[i][r] > maior:
                    maior = matriz[i][r]
                r += 1
        i += 1

    return maior


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(encontra_maximo(a))