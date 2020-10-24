def encontra_maximo (matriz):
    maximo = 0
    for linha in matriz:
        for valor in linha:
            if abs(valor)>maximo:
                maximo = valor
    return maximo