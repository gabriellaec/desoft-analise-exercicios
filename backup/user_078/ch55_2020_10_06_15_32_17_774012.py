def encontra_maximo(matriz):
    recorde = 0

    for linha in matriz:
        for numero in linha:

            if numero > recorde:
                recorde = numero
    
    return recorde