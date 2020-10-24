def encontra_maximo(lista):
    max_ = 0
    for i in lista:
        for j in i:
            if j>max_:
                max_ = j
    return max_