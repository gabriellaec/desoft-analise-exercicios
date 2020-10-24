def encontra_maximo(matriz):
    lista = []
    for i in matriz:
        for t in i:
            lista.append(abs(t))
    return max(lista)