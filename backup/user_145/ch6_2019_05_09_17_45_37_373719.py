def encontra_maximo(matriz):
    maior = 0
    for lista in matriz:
        for e in lista:
            if e > maior:
                maior = e
                return maior

