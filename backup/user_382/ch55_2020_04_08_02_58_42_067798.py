def encontra_maximo(lista):
    lista2 = []
    for i in lista:
        for t in i:
            lista2.append(t)
    return max(lista2)