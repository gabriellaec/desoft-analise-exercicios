def encontra_maximo(matriz):
    maior = 0
    for im in range(len(matriz)):
        for il in range(len(matriz[im])):
            if im[il] > im[il-1]:
                maior == im[il]
    return maior