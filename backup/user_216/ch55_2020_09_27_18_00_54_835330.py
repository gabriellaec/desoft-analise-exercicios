def encontra_maximo(lista):
    maior_valor = lista[0][0]
    i = 0
    while i < 3:
        for e in range(0,3):
            if lista[i][e] > maior_valor:
                maior_valor = lista[i][e]
        i += 1
    return maior_valor