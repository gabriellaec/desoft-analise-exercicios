def encontra_maximo(matriz):
    maior = 0
    for linha in matriz:
        if max(linha) > maior:
        	maior = max(linha)
    return maior