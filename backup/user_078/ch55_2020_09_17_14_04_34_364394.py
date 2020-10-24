
def encontra_maximo(matriz):
    i = 0
    maior_valor = 0

    for i in matriz:
        for z in i:
            
            if z > maior_valor:
                maior_valor = z

    return maior_valor