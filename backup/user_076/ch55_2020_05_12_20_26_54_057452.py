def encontra_maximo (matriz):
    maximo = 0
    for linha in matriz:
        for valor in linha:
            if valor>maximo:
                maximo = valor
    return maximo