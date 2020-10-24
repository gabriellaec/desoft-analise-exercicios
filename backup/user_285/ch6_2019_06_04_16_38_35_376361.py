def encontra_maximo(matriz):
    maior=0
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior=elemento
    return maior

        