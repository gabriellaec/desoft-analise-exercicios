def encontra_maximo(matriz):
    maximo = []
    for c in matriz:
        for i in c:
            maximo.append(i)
    return max(maximo)