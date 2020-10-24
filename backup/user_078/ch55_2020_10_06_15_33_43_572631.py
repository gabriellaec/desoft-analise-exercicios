def encontra_maximo(matriz):

    for linha in matriz:
        for numero in linha:

            if numero > recorde:
                recorde = numero
    
    return recorde