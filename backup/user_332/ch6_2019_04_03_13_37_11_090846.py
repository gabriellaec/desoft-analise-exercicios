def encontra_maximo(lista):
    maior = lista[0][0]
    i = 0
    while i < 3 :
        a = 0
        while a < 3:
            if lista[i][a] > maior:
                maior = lista[i][a]
            a += 1
        i += 1
    return maior