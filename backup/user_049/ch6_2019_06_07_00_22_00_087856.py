def encontra_maximo(matriz):
    max_valor = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            matriz[linha][coluna]=(matriz[linha][coluna]**2)**0.5
            if max_valor < matriz[linha][coluna]:
                max_valor = matriz[linha][coluna]
    return max_valor