def encontra_maximo(lista):
    maior = 0
    for i in lista:
        for z in i:
            if z > maior:
                maior = z
    return maior