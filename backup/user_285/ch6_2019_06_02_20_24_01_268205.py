def encontra_maximo(matriz):
    maior=0
    for linha in range matriz:
        for coluna in range matriz[linha]:
            if matriz[linha][coluna]>maior:
                maior=matriz[linha][coluna] 
                return maior

        