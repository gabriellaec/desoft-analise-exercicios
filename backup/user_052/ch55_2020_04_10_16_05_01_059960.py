def encontra_maximo (matriz):
    lista2 = []
    for i in matriz:
        for t in i:
            lista2.append(abs(t))
    return max(lista2)