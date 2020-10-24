def encontra_maximo(lista):
    max = 0
    for i in lista:
        for j in i:
            if j>max:
                max = j
    return max