def encontra_maximo(matriz):
    maior=0
    for linha in range(len(matriz)):
        for coluna in matriz[linha]:
            if matriz[linha][coluna]>maior:
                maior=matriz[linha][coluna] 
    return maior

        