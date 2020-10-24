def encontra_maximo(matriz):
    maior=0
    for linha in range(3):
        for coluna in range(3):
            if (matriz[linha][coluna])**2>(maior)**2:
                maior=matriz[linha][coluna]
    return maior

        