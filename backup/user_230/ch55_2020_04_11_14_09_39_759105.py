def encontra_maximo(matriz):
    maior_linha = 0
    maior_coluna = 0
    maior = matriz[0][0]
    for l in range(4):
        for c in range(4):        
            if maior < matriz[l][c]:
                maior = matriz[l][c]
                maior_linha = l
                maior_coluna = c
    