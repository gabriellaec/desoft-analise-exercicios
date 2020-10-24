def encontra_maximo(matriz):
    maior=0
    for linha in range(3):
        for coluna in range(3):
            if abs(matriz[linha][coluna])>abs(maior):
                maior=matriz[linha][coluna]
    return maior

        