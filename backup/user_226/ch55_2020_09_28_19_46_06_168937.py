def encontra_maximo(lista):
    maior_valor = lista[0][0]
    i = 0
    while i < 3:
        z = 0
        while z < 3:
            if lista[i][z] < 0:
                lista[i][z] = -(lista[i][z])
            if lista[i][z] > maior_valor:
                maior_valor = lista[i][z]
            z += 1
        i += 1
    return maior_valor