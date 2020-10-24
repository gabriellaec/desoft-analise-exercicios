def encontra_maximo(matriz):
    maximo = []
    for c in matriz:
        for i in c:
            maximo.append(float(i))
    return max(maximo)