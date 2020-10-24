def encontra_maximo(matriz):
    maior=0
    for linha in matriz:
        for indice in range(len(linha)):
            if abs(linha[indice]) > maior:
                maior=abs(linha[indice]) 
    return maior

        